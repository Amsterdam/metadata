from django.conf.urls import url, include
from django.contrib import admin

import atlas.urls


urlpatterns = [
    url(r'', include(atlas.urls.router.urls)),

    url(r'^metadata-admin/', admin.site.urls),
    url(r'^status/', include('datapunt_generic.health.urls', namespace='health')),
]
