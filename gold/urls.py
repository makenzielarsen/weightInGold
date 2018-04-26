from django.urls import path
from gold import views

urlpatterns = [
    path('', views.weight),
]
