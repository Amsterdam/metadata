from django.contrib import admin

from .models import MetaData


class MetaDataAdmin(admin.ModelAdmin):
    exclude = ('',)
    def get_queryset(self, request):
        return MetaData.objects.all().exclude(title=u'')


admin.site.register(MetaData, MetaDataAdmin)
