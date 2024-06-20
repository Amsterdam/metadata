from django.shortcuts import get_object_or_404

from rest_framework import mixins, viewsets

from .models import MetaData
from .serializers import MetaDataSerializer


class MetaDataViewset(
    mixins.UpdateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    serializer_class = MetaDataSerializer
    queryset = MetaData.objects.all().exclude(title__isnull=True)
    lookup_value_regex = "[^/]+"

    def get_object(self):
        obj = get_object_or_404(MetaData, pk=self.kwargs["pk"])

        return obj
