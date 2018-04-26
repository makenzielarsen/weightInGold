from django.urls import path
from api import views

urlpatterns = [
    path('init/', views.init),
    path('convert/', views.convert),
]
