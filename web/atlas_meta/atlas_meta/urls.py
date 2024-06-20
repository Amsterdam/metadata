from django.urls import path
from django.urls import re_path, include
from django.contrib import admin

import atlas.urls


urlpatterns = [
    path("", include(atlas.urls.router.urls)),
    re_path(r"^metadata-admin/", admin.site.urls),
    path("status/", include("datapunt_generic.health.urls", namespace="health")),
]
