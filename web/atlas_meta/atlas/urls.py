from rest_framework import routers

import atlas.views as views


class AtlasRouter(routers.DefaultRouter):
    """
    Atlas metadata API.
    """


router = AtlasRouter()
router.register(r'metadata', views.MetaDataViewset, base_name='metadata')

urlpatterns = router.urls
