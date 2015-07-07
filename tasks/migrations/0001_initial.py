# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_due', models.DateField(verbose_name=b'date due')),
                ('person_in_charge', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('task_type', models.ForeignKey(to='auth.Group')),
            ],
        ),
    ]
