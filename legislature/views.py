from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import re


# Create your views here.


@login_required
def home(request):
    if request.user.id is not None:
        fn = request.user.ldap_user.attrs.get("displayName", [])[0]
        request.user.fn = fn
        request.user.memberOf = parse_groups(request.user)

    return render(request, 'index.html')


@login_required
def profile(request):
    if request.user.id is not None:
        fn = request.user.ldap_user.attrs.get("displayName", [])[0]
        request.user.fn = fn
        email = request.user.ldap_user.attrs.get("mail", [])[0]
        desc = request.user.ldap_user.attrs.get("description", [])[0]
        request.user.email = email
        request.user.desc = desc
        desc = request.user.ldap_user.attrs.get("description", [])[0]
        request.user.memberOf = parse_groups(request.user)
        request.user.desc = desc

    return render(request, 'profile.html')


def parse_groups(user):
    memberOf = user.ldap_user.attrs.get("memberOf", [])
    groups = []
    groupList = []
    for group in memberOf:
        groups.append(re.findall(r'CN=(.*?),OU', group))
    for group in groups:
        groupList.append(group[0])

    return groupList
