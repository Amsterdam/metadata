# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-21 12:18
from __future__ import unicode_literals

from django.db import migrations


def create_initial_data(apps, schema_editor):
    user_model = apps.get_model('auth', 'user')

    user = user_model(
        username='test@test.com',
        password='atlas123',
        is_active=True,
        is_superuser=True,
        is_staff=True,
    )

    user.save()


class Migration(migrations.Migration):

    dependencies = [
        ('atlas', '0002_initial_data'),
    ]

    operations = [
        migrations.RunPython(create_initial_data),
    ]