# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, help_text='\u4e3b\u952eid', unique=True)),
                ('name', models.CharField(help_text='\u4f1a\u5458\u59d3\u540d', max_length=5)),
                ('tel', models.CharField(help_text='\u4f1a\u5458\u624b\u673a\u53f7', max_length=11)),
                ('account', models.FloatField(default=0.0, help_text='\u8d26\u6237\u4f59\u989d', verbose_name='\u53ef\u662f\u5bf9\u65b9')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MemberType',
            fields=[
                ('id', models.AutoField(unique=True, serialize=False, primary_key=True)),
                ('typename', models.CharField(max_length=5)),
                ('status', models.BooleanField(default=True)),
                ('createtime', models.DateTimeField(auto_now_add=True)),
                ('updatetime', models.TimeField(auto_now=True, auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='member',
            name='member_type',
            field=models.ForeignKey(to='myapp.MemberType'),
            preserve_default=True,
        ),
    ]
