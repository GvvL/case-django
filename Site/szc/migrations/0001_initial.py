# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SzcAddr',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('member_id', models.IntegerField()),
                ('address_linkman', models.CharField(max_length=5)),
                ('address_linktel', models.CharField(max_length=11, blank=True)),
                ('address_detail', models.CharField(max_length=30)),
                ('status', models.IntegerField()),
                ('isdefault', models.IntegerField()),
            ],
            options={
                'db_table': 'szc_addr',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SzcBanners',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50, blank=True)),
                ('title', models.CharField(max_length=255, blank=True)),
                ('link', models.CharField(max_length=255, blank=True)),
                ('typeid', models.IntegerField(null=True, blank=True)),
                ('status', models.IntegerField(null=True, blank=True)),
                ('img', models.CharField(max_length=255, blank=True)),
            ],
            options={
                'db_table': 'szc_banners',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SzcBannerType',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50, blank=True)),
                ('status', models.IntegerField(null=True, blank=True)),
                ('position', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'szc_banner_type',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SzcCarousel',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column='Id')),
                ('img', models.CharField(max_length=255)),
                ('target', models.CharField(max_length=255)),
                ('valid', models.IntegerField()),
            ],
            options={
                'db_table': 'szc_carousel',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SzcChefs',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('photo', models.CharField(max_length=255)),
                ('img', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('styleid', models.IntegerField()),
                ('monicker', models.CharField(max_length=100)),
                ('grade', models.FloatField()),
                ('vedio', models.CharField(max_length=255)),
                ('supporter', models.IntegerField(null=True, blank=True)),
                ('status', models.IntegerField()),
            ],
            options={
                'db_table': 'szc_chefs',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SzcCoupons',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('uid', models.IntegerField()),
                ('value', models.FloatField()),
                ('min', models.FloatField()),
                ('valid_date', models.IntegerField()),
                ('status', models.IntegerField()),
            ],
            options={
                'db_table': 'szc_coupons',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SzcDishes',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('img', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=50)),
                ('en', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=255)),
                ('chef_id', models.IntegerField()),
                ('favors', models.IntegerField()),
                ('price', models.FloatField()),
                ('vedio', models.CharField(max_length=255)),
                ('recommended', models.IntegerField()),
                ('status', models.IntegerField()),
                ('num', models.IntegerField()),
                ('sales', models.IntegerField()),
                ('vipprice', models.FloatField()),
                ('type', models.IntegerField()),
                ('style', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'szc_dishes',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SzcDishTypes',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=20)),
                ('benable', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'szc_dish_types',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SzcGroup',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('lower', models.CharField(max_length=2000)),
                ('status', models.IntegerField()),
                ('description', models.CharField(max_length=255, blank=True)),
            ],
            options={
                'db_table': 'szc_group',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SzcMemberAddress',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('uid', models.IntegerField()),
                ('uname', models.CharField(max_length=50)),
                ('tel', models.CharField(max_length=20)),
                ('addr', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'szc_member_address',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SzcMembers',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('photo', models.CharField(max_length=255)),
                ('uname', models.CharField(max_length=20)),
                ('nick', models.CharField(max_length=255)),
                ('pwd', models.CharField(max_length=32)),
                ('tel', models.CharField(max_length=20)),
                ('addr_id', models.IntegerField()),
                ('balance', models.FloatField()),
                ('last_ip', models.CharField(max_length=255)),
                ('last_time', models.IntegerField()),
                ('status', models.IntegerField()),
                ('type', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'szc_members',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SzcModule',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('active', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=20)),
                ('level', models.IntegerField()),
                ('status', models.IntegerField(null=True, blank=True)),
                ('iconfont', models.CharField(max_length=10, blank=True)),
            ],
            options={
                'db_table': 'szc_module',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SzcOrderDetail',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('order_id', models.IntegerField()),
                ('dish_id', models.IntegerField()),
                ('title', models.CharField(max_length=255)),
                ('price', models.FloatField()),
                ('count', models.IntegerField()),
            ],
            options={
                'db_table': 'szc_order_detail',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SzcOrders',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('sn', models.CharField(max_length=17)),
                ('uid', models.IntegerField()),
                ('uname', models.CharField(max_length=50)),
                ('tel', models.CharField(max_length=20)),
                ('addr', models.CharField(max_length=255)),
                ('addrid', models.IntegerField(null=True, blank=True)),
                ('couponid', models.IntegerField(null=True, blank=True)),
                ('price', models.FloatField()),
                ('paied', models.FloatField()),
                ('order_time', models.IntegerField()),
                ('pay_time', models.IntegerField(null=True, blank=True)),
                ('pay_channel', models.CharField(max_length=10, blank=True)),
                ('isnew', models.IntegerField()),
                ('status', models.IntegerField()),
                ('note', models.TextField(blank=True)),
                ('district', models.CharField(max_length=12, blank=True)),
                ('from_field', models.IntegerField(db_column='from')),
                ('order_freight', models.FloatField()),
            ],
            options={
                'db_table': 'szc_orders',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SzcPowers',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50, blank=True)),
                ('lower', models.TextField(blank=True)),
                ('status', models.IntegerField(null=True, blank=True)),
                ('description', models.CharField(max_length=255, blank=True)),
            ],
            options={
                'db_table': 'szc_powers',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SzcRechargeRecord',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('recharge_sn', models.CharField(max_length=20)),
                ('member_id', models.IntegerField()),
                ('value', models.IntegerField()),
                ('create_time', models.CharField(max_length=11)),
                ('end_time', models.CharField(max_length=11)),
                ('status', models.IntegerField()),
                ('pay_channel', models.CharField(max_length=5, blank=True)),
                ('paid', models.FloatField(null=True, blank=True)),
            ],
            options={
                'db_table': 'szc_recharge_record',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SzcRechargeType',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('value', models.IntegerField()),
                ('status', models.IntegerField()),
            ],
            options={
                'db_table': 'szc_recharge_type',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SzcStyle',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=255, blank=True)),
                ('benable', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'szc_style',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SzcUser',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('uname', models.CharField(max_length=50)),
                ('nickname', models.CharField(max_length=50, blank=True)),
                ('pwd', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50, blank=True)),
                ('tel', models.BigIntegerField(null=True, blank=True)),
                ('area_name', models.CharField(max_length=20, blank=True)),
                ('area_id', models.CharField(max_length=20, blank=True)),
                ('group_id', models.IntegerField()),
                ('pid', models.IntegerField()),
                ('sid', models.IntegerField()),
                ('last_ip', models.CharField(max_length=20, blank=True)),
                ('last_time', models.IntegerField(null=True, blank=True)),
                ('status', models.IntegerField()),
            ],
            options={
                'db_table': 'szc_user',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SzcZone',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('zone_id', models.IntegerField(null=True, blank=True)),
                ('zone_name', models.CharField(max_length=50, blank=True)),
                ('level', models.IntegerField(null=True, blank=True)),
                ('end', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'szc_zone',
                'managed': False,
            },
            bases=(models.Model,),
        ),
    ]
