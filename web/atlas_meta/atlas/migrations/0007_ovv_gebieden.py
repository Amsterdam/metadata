from django.db import migrations, IntegrityError
from django.core.exceptions import ObjectDoesNotExist

NEW_DATA = (
    {
        'id': 'gebieden-ovv',
        'title': 'Overlastgebieden',
        'group': '680',
        'update_frequency': 'op verzoek',
        'data_modified_date': 'augustus 2018',
    },
)


def update_ovv_gebieden(apps, schema_editor):
    Migrations = apps.get_model('atlas', 'metadata')

    # Delete gebieden_ovv, if it exists
    try:
        gebieden_ovv = Migrations.objects.get(pk='gebieden-ovv')
    except ObjectDoesNotExist:
        pass  # this row doesn't exist
    else:
        gebieden_ovv.delete()

    # insert the splitted rows, if they don't exist
    for row in NEW_DATA:
        try:
            Migrations.objects.create(**row)
        except IntegrityError:
            pass  # a row with this PK already exists.


class Migration(migrations.Migration):

    dependencies = [
        ('atlas', '0006_nap_meetbouten'),
    ]

    operations = [
        migrations.RunPython(update_ovv_gebieden),
    ]
