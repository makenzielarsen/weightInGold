from django.shortcuts import render, redirect
from api.models import Conversion
from django.http import JsonResponse

# goldRUrl = "https://www.quandl.com/api/v3/datasets/LBMA/GOLD.json?api_key=yohchH9Uyg7_EzdN6cJP&column_index=2&start_date=2018-02-04&end_date=2018-02-09"


def convert(request):
    to_units = request.GET.get('to', 't_oz')
    from_units = request.GET.get('from', 'lbs')
    value = request.GET.get('value', '2.2')
    results = Conversion.objects.filter(
        to_units=to_units, from_units=from_units)
    if len(results) == 0:
        return JsonResponse({"error": "Invalid type conversion!"})
    return JsonResponse({"units": to_units, "value": float(value) * results[0].value})


def init(request):
    table = {"mg": {"g": 1000, "kg": 1000000, "t_oz": 0.0000321507, "oz": 28349.5, "lbs": 453592, "ton": 907185000},
             "g": {"mg": 0.001, "kg": 1000, "t_oz": 0.0321507, "oz": 28.3495, "lbs": 453.592, "ton": 907185},
             "kg": {"mg": 0.00001, "g": 0.001, "t_oz": 32.1507, "oz": 0.0283495, "lbs": 0.453592, "ton": 907.185},
             "t_oz": {"mg": 31103.5, "g": 31.1035, "kg": 0.0311035, "oz": 1.09714, "lbs": 0.0685714, "ton": 0.0000342857},
             "oz": {"mg": 0.000035274, "g": 0.035274, "kg": 35.274, "t_oz": 0.911458, "lbs": 16, "ton": 32000},
             "lbs": {"mg": 0.000000022046, "g": 0.00220462, "kg": 2.20462, "t_oz": 14.5833, "oz": 0.0625, "ton": 2000},
             "ton": {"mg": 907200000, "g": 1.10231E-06, "kg": 0.00110231, "t_oz": 29166.7, "oz": 0.00003125, "lbs": 0.0005}}
    for from_unit, inner in table.items():
        for to_unit, value in inner.items():
            temp = Conversion(to_units=to_unit,
                              from_units=from_unit, value=value)
            temp.save()
    return redirect('http://127.0.0.1:8000/api/convert/?from=lbs&to=t_oz&value=120')
