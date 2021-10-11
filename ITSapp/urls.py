from django.urls import path

from ITSapp.views import ITS

app_name = "ITSapp"

urlpatterns = [
    path('ITS/', ITS, name='ITS')
]