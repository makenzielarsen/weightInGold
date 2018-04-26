from django.db import models


class Conversion(models.Model):
    to_units = models.CharField(default="", max_length=100)
    from_units = models.CharField(default="", max_length=100)
    value = models.FloatField()
