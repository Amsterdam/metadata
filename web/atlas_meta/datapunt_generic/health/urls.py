from django.urls import re_path

from . import views

app_name = 'datapunt-health'

urlpatterns = [
    re_path(r'^health$', views.health),
    re_path(r'^data$', views.check_data),
]
