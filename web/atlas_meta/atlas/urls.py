from django.conf.urls import url, include
from rest_framework import routers

import atlas.views as views
from atlas_meta import settings


class AtlasRouter(routers.DefaultRouter):
    """
    Atlas metadata API.
    """


router = AtlasRouter()
router.register(r'metadata', views.MetaDataViewset, base_name='metadata')

urlpatterns = router.urls

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
