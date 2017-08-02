from django.db import models


class LegApplications(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    adGroup = models.CharField(max_length=100)

    def __str__(self):
        return '%s' % (self.description)

    class Meta:
        app_label = 'leg_app'
