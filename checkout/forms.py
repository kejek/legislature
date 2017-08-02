__author__ = 'cla283'
from django import forms
from checkout.models import Status
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class CheckoutForm(forms.Form):
    STATUS_CHOICES = [(status.statusId, status.desc.capitalize())
                      for status in Status.objects.all()]
    notes = forms.CharField(label='Note', max_length=150,
                            required=False)
    site = forms.CharField(label='Site', max_length=150,
                           required=False)
    site_phone = forms.CharField(label='Site Phone',
                                 max_length=150, required=False)
    status = forms.ChoiceField(
        label='Status',
        choices=STATUS_CHOICES, widget=forms.RadioSelect()
    )

    def __init__(self, *args, **kwargs):
        super(CheckoutForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = '/checkout/'

        self.helper.add_input(Submit('submit', 'Submit'))
