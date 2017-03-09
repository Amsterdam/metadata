'''
Created on 9 Jan 2017

@author: evert
'''

from django.db import migrations, IntegrityError
from django.core.exceptions import ObjectDoesNotExist

NEW_DATA = (
    {
        'id': 'nap',
        'title': 'NAP',
        'group': 'NAP',
        'update_frequency': 'op verzoek',
        'data_modified_date': 'op verzoek',
    },
    {
        'id': 'meetbouten',
        'title': 'Meetbouten',
        'group': 'NAP',
        'update_frequency': 'op verzoek',
        'data_modified_date': 'op verzoek',
    },
)


def update_nap_meetbouten(apps, schema_editor):
    Migrations = apps.get_model('atlas', 'metadata')

    # Delete nap-meetbouten, if it exists
    try:
        nap_meetbouten = Migrations.objects.get(pk='nap-meetbouten')
    except ObjectDoesNotExist:
        pass  # this row doesn't exist
    else:
        nap_meetbouten.delete()

    # insert the splitted rows, if they don't exist
    for row in NEW_DATA:
        try:
            Migrations.objects.create(**row)
        except IntegrityError:
            pass  # a row with this PK already exists.


class Migration(migrations.Migration):

    dependencies = [
        ('atlas', '0005_auto_20160407_1213'),
    ]

    operations = [
        migrations.RunPython(update_nap_meetbouten),
    ]
