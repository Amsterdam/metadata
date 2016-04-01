from rest_framework import mixins, viewsets

from .models import MetaData
from .serializers import MetaDataSerializer


class MetaDataViewset(mixins.UpdateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = MetaDataSerializer
    queryset = MetaData.objects.all().exclude(title=u'')
    lookup_value_regex = '[^/]+'
