from rest_framework import serializers

from .models import MetaData


class MetaDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetaData
        fields = "__all__"

    def update(self, instance, validated_data):
        data_modified_date = validated_data.get("data_modified_date")
        last_import_date = validated_data.get("last_import_date")

        instance.data_modified_date = data_modified_date
        instance.last_import_date = last_import_date
        instance.save()

        return instance
