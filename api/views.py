from django.http import HttpResponse
from django.shortcuts import render

from django_site import settings


# Create your views here.
def get_app_info(request):
    return HttpResponse(f"App version: {settings.APP_VERSION}")
