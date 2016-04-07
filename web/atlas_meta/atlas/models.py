from django.db import models


class MetaData(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    group = models.CharField(max_length=100, null=True, blank=True)
    update_frequency = models.CharField(max_length=100, null=True, blank=True)
    data_modified_date = models.CharField(
        max_length=100, null=True, blank=True)
    last_import_date = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ('-group', 'title')

    def __str__(self):
        if self.group:
            return '{} - {}'.format(self.group, self.title)

        return self.title
