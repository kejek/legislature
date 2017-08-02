from django.shortcuts import render
from forms import CheckoutForm
from django.http import Http404, HttpResponse, JsonResponse, \
    HttpResponseRedirect
from django.core import serializers
from django.views.generic import View
from checkout.models import Employee
from checkout.models import Status
from checkout.models import Section
from checkout.models import Group
from checkout.models import Division
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
import re
import json


# Create your views here.


class CheckoutFormView(View):
    form_class = CheckoutForm
    initial = {'key': 'value'}
    template_name = 'checkout/index.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        employee = Employee()
        if request.user.id is not None:
            employee = check_if_user_exists(request.user)
            fn = extract_attribute(
                request.user.ldap_user.attrs.get("displayName", []))
            request.user.fn = fn
            request.user.memberOf = parse_groups(request.user)

        context = load_checkout_context(form, employee, request)
        if request.is_ajax():
            return render(request, 'checkout/results.html', context)
        else:
            return render(request, self.template_name, context)

    @method_decorator(login_required())
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        employee = Employee()
        if request.user.id is not None:
            employee = check_if_user_exists(request.user)
            fn = extract_attribute(
                request.user.ldap_user.attrs.get("displayName", []))
            request.user.fn = fn
            request.user.memberOf = parse_groups(request.user)

        context = load_checkout_context(form, employee, request)
        if form.is_valid():
            # <process form cleaned data>
            status = form.cleaned_data['status']
            notes = form.cleaned_data['notes']
            site = form.cleaned_data['site']
            site_phone = form.cleaned_data['site_phone']

            employee.status = Status.objects.get(statusId=status)
            employee.notes = notes
            employee.site = site
            employee.site_phone = site_phone
            employee.save()
            return HttpResponseRedirect('/checkout/')

        return render(request, self.template_name, context)


def parse_groups(user):
    memberOf = user.ldap_user.attrs.get("memberOf", [])
    groups = []
    groupList = []
    for group in memberOf:
        groups.append(re.findall(r'CN=(.*?),OU', group))
    for group in groups:
        groupList.append(group[0])

    return groupList


def check_if_user_exists(user):
    try:
        employee = Employee.objects.get(user=user.get_username())
        # user exists, update information
        employee = update_employee_information(employee, user)
    except Employee.DoesNotExist:
        employee = populate_new_employee(user)
    return employee


def update_employee_information(employee, user):
    employee.name = extract_attribute(
        user.ldap_user.attrs.get("displayName", []))
    employee.email = extract_attribute(user.ldap_user.attrs.get("mail", []))
    employee.phone = extract_attribute(
        user.ldap_user.attrs.get("telephoneNumber", []))
    try:
        group = Group.objects.get(
            name=extract_attribute(user.ldap_user.attrs.get("description", [])))
    except Group.DoesNotExist:
        group = create_new_group(
            extract_attribute(user.ldap_user.attrs.get("description", [])))
    employee.group = group
    employee.section = Section.objects.get(id=1)
    employee.save()
    return employee


def populate_new_employee(user):
    employee = Employee()
    employee.name = extract_attribute(
        user.ldap_user.attrs.get("displayName", []))
    employee.email = extract_attribute(user.ldap_user.attrs.get("mail", []))
    employee.phone = extract_attribute(
        user.ldap_user.attrs.get("telephoneNumber", []))
    employee.site = ""
    employee.site_phone = ""
    employee.user = user.get_username()
    employee.status = Status.objects.get(statusId=1)
    try:
        group = Group.objects.get(
            name=extract_attribute(user.ldap_user.attrs.get("description", [])))
    except Group.DoesNotExist:
        group = create_new_group(
            extract_attribute(user.ldap_user.attrs.get("description", [])))
    employee.group = group
    employee.section = Section.objects.get(id=1)
    employee.save()
    return employee


def create_new_group(description):
    group = Group()
    group.name = description
    group.description = description
    group.save()
    return group


def extract_attribute(attribute):
    try:
        attr = attribute[0]
    except IndexError:
        attr = ""
    return attr


def load_checkout_context(form, employee, request):
    # Gets all Employee Checkout Information
    employeeList = [];

    sections = Section.objects.all().select_related("division")
    groups = Group.objects.all()
    statusList = Status.objects.all()
    if request.is_ajax():
        q = request.GET.get('q')
        if q is not None:
            for group in groups:
                for section in sections:
                    employees = Employee.objects.filter(group=group.id) \
                        .filter(section=section.id).filter(
                        Q(name__contains=q) | Q(
                            user__contains=q)).select_related("status") \
                        .select_related("section").order_by('group')
                    if len(employees):
                        employeeList.append(employees)
        else:
            for group in groups:
                for section in sections:
                    employees = Employee.objects.filter(group=group.id) \
                        .filter(section=section.id).select_related("status") \
                        .select_related("section").order_by('group')
                    if len(employees):
                        employeeList.append(employees)
    else:
        for group in groups:
            for section in sections:
                employees = Employee.objects.filter(group=group.id) \
                    .filter(section=section.id).select_related("status") \
                    .select_related("section").order_by('group')
                if len(employees):
                    employeeList.append(employees)
    divisions = Division.objects.all()
    # sorts list via section name. Possibly better to use Database design
    # or queries to do this?
    employeeList = sorted(employeeList, key=lambda emp: emp[0].section.name)

    context = {
        'form': form,
        'employeeList': employeeList,
        'sections': sections,
        'groups': groups,
        'divisions': divisions,
        'statusList': statusList,
        'employee': employee,
        'secId': 0,  # required for section label
    }
    return context


class AllEmployeesApi(View):
    @method_decorator(login_required())
    def get(self, request, *args, **kwargs):
        employees = Employee.objects.all().select_related('status')
        data = serializers.serialize('json', employees)
        data = json.dumps(json.loads(data), indent=4)
        return HttpResponse(data, content_type='application/json')


class RefreshModalData(View):
    form_class = CheckoutForm
    initial = {'key': 'value'}
    template_name = 'checkout/index.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        employee = Employee()
        if request.user.id is not None:
            employee = check_if_user_exists(request.user)
            fn = extract_attribute(
                request.user.ldap_user.attrs.get("displayName", []))
            request.user.fn = fn
            request.user.memberOf = parse_groups(request.user)

        context = load_checkout_context(form, employee, request)
        if request.is_ajax():
            return render(request, 'checkout/modalData.html', context)
        else:
            return render(request, self.template_name, context)
