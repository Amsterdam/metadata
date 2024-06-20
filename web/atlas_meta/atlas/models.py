from django.db import models


class MetaData(models.Model):
    id = models.CharField(max_length=255, primary_key=True)

    title = models.CharField(
        max_length=100, null=True, blank=True, help_text="Titel thema"
    )

    group = models.CharField(
        max_length=100, null=True, blank=True, help_text="Thema groep (optioneel)"
    )

    update_frequency = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        help_text="Actualisatie (aanmaak producten)",
    )

    data_modified_date = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        help_text="Versie datum gegevens (peildatum verwerkt product)",
    )

    last_import_date = models.DateField(
        null=True,
        blank=True,
        help_text="Laatst geimporteerd (wordt automatisch gevuld) / YYYY-MM-DD",
    )

    class Meta:
        ordering = ("-group", "title")

    def __str__(self):
        if self.group:
            return "{} - {}".format(self.group, self.title)

        return self.title or "<empty>"
