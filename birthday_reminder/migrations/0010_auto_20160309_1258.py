# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-09 20:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('birthday_reminder', '0009_auto_20160308_1716'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='email_bool',
            new_name='send_email',
        ),
    ]
