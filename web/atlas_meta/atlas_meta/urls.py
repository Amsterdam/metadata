from django.urls import re_path, include
from django.contrib import admin

import atlas.urls


urlpatterns = [
    re_path(r'', include(atlas.urls.router.urls)),

    re_path(r'^metadata-admin/', admin.site.urls),
    re_path(r'^status/', include('datapunt_generic.health.urls', namespace='health')),
]
