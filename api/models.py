from django.db import models


class Conversion(models.Model):
    units = models.TextField()
    value = models.FloatField()
