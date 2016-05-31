# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('szc', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='szcorderdetail',
            options={'managed': False, 'verbose_name': '\u8ba2\u5355\u8be6\u60c5'},
        ),
        migrations.AlterModelOptions(
            name='szcorders',
            options={'managed': False, 'verbose_name': '\u8ba2\u5355\u5217\u8868'},
        ),
    ]
