__author__ = 'cla283'
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.CheckoutFormView.as_view(), name='index'),
    url(r'^employees/', views.AllEmployeesApi.as_view(),
        name='allEmployeesToJson'),
    url(r'^refreshModalData/', views.RefreshModalData.as_view(),
        name='refreshModalData'),
]
