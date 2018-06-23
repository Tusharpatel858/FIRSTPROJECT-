"""Defines URL patterns for FIRSTAPPLICATION."""
from django.conf.urls import url
from . import views

urlpatterns = [
    # Home page
    url('index/', views.index, name='index'),
    url('static-img/', views.img , name='img'),
]
