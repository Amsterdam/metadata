from django.urls import path

from . import views

app_name = "datapunt-health"

urlpatterns = [
    path("health", views.health),
    path("data", views.check_data),
]
