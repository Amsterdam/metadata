from django.contrib import admin

from .models import MetaData


class MetaDataAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'group', 'update_frequency', 'data_modified_date', 'last_import_date']

    def get_queryset(self, request):
        return MetaData.objects.exclude(title__isnull=True)


admin.site.register(MetaData, MetaDataAdmin)
