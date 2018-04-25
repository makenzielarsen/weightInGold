from django.shortcuts import render
from api.models import Conversion
from django.core import serializers
from django.shortcuts import HttpResponse


def convert(request):
    conversion = Conversion()
    conversion.units = request.GET.get('to', 't_oz')
    from_units = request.GET.get('from', 'lbs')
    from_value = request.GET.get('value', '2.2')
    conversion.value = from_value
    # goldRUrl = "https://www.quandl.com/api/v3/datasets/LBMA/GOLD.json?api_key=yohchH9Uyg7_EzdN6cJP&column_index=2&start_date=2018-02-04&end_date=2018-02-09"
    data = serializers.serialize(
        'json', [conversion], fields=('units', 'value'))
    return HttpResponse(data, content_type="application/json")
