from django.db import models
from django.contrib.auth.models import User

class Status(models.Model):
    desc = models.CharField(max_length=100)
    statusId = models.CharField(max_length=100)

    def __str__(self):
        return '%s' % (self.desc)

    class Meta:
        app_label = 'checkout'


class Division(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return '%s' % (self.name)

    class Meta:
        app_label = 'checkout'


class Group(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return '%s' % (self.name)

    class Meta:
        app_label = 'checkout'


class Section(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    division = models.ForeignKey(Division)

    def __str__(self):
        return '%s' % (self.name)

    class Meta:
        app_label = 'checkout'


class Employee(models.Model):
    name = models.CharField(max_length=250)
    image = models.FileField(null=True, blank=True)
    phone = models.CharField(max_length=12, blank=True)
    notes = models.TextField(blank=True)
    status = models.ForeignKey(Status)
    returning = models.TextField(blank=True)
    section = models.ForeignKey(Section)
    group = models.ForeignKey(Group)
    user = models.CharField(max_length=50, null=True)
    site_phone = models.CharField(max_length=20, blank=True, null=True)
    site = models.CharField(max_length=100, blank=True, null=True)
    schedule = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return '%s' % (self.name)

    class Meta:
        app_label = 'checkout'