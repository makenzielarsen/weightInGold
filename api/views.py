from django.shortcuts import render
from api.models import Conversion
from django.core import serializers
from django.shortcuts import HttpResponse


def convert(request):
    conversion = Conversion()
    conversion.units = "lbs"
    conversion.value = 2.2
    data = serializers.serialize('json', [conversion])
    return HttpResponse(data, content_type="application/json")
