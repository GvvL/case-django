#coding:utf-8
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.

from __future__ import unicode_literals

from django.db import models


class SzcAddr(models.Model):
    id = models.AutoField(primary_key=True)  # AutoField?
    member_id = models.IntegerField()
    address_linkman = models.CharField(max_length=5)
    address_linktel = models.CharField(max_length=11, blank=True)
    address_detail = models.CharField(max_length=30)
    status = models.IntegerField()
    isdefault = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'szc_addr'


class SzcBannerType(models.Model):
    id = models.AutoField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=50, blank=True)
    status = models.IntegerField(blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'szc_banner_type'


class SzcBanners(models.Model):
    id = models.AutoField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=50, blank=True)
    title = models.CharField(max_length=255, blank=True)
    link = models.CharField(max_length=255, blank=True)
    typeid = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    img = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'szc_banners'


class SzcCarousel(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    img = models.CharField(max_length=255)
    target = models.CharField(max_length=255)
    valid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'szc_carousel'


class SzcChefs(models.Model):
    id = models.AutoField(primary_key=True)  # AutoField?
    photo = models.CharField(max_length=255)
    img = models.CharField(max_length=255)
    name = models.CharField(max_length=50)
    description = models.TextField()
    styleid = models.IntegerField()
    monicker = models.CharField(max_length=100)
    grade = models.FloatField()
    vedio = models.CharField(max_length=255)
    supporter = models.IntegerField(blank=True, null=True)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'szc_chefs'


class SzcCoupons(models.Model):
    id = models.AutoField(primary_key=True)  # AutoField?
    uid = models.IntegerField()
    value = models.FloatField()
    min = models.FloatField()
    valid_date = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'szc_coupons'


class SzcDishTypes(models.Model):
    id = models.AutoField(primary_key=True)  # AutoField?
    title = models.CharField(max_length=20)
    benable = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'szc_dish_types'


class SzcDishes(models.Model):
    id = models.AutoField(primary_key=True)  # AutoField?
    img = models.CharField(max_length=255)
    title = models.CharField(max_length=50)
    en = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    chef_id = models.IntegerField()
    favors = models.IntegerField()
    price = models.FloatField()
    vedio = models.CharField(max_length=255)
    recommended = models.IntegerField()
    status = models.IntegerField()
    num = models.IntegerField()
    sales = models.IntegerField()
    vipprice = models.FloatField()
    type = models.IntegerField()
    style = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'szc_dishes'


class SzcGroup(models.Model):
    id = models.AutoField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=50)
    lower = models.CharField(max_length=2000)
    status = models.IntegerField()
    description = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'szc_group'


class SzcMemberAddress(models.Model):
    id = models.AutoField(primary_key=True)  # AutoField?
    uid = models.IntegerField()
    uname = models.CharField(max_length=50)
    tel = models.CharField(max_length=20)
    addr = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'szc_member_address'


class SzcMembers(models.Model):
    id = models.AutoField(primary_key=True)  # AutoField?
    photo = models.CharField(max_length=255)
    uname = models.CharField(max_length=20)
    nick = models.CharField(max_length=255)
    pwd = models.CharField(max_length=32)
    tel = models.CharField(max_length=20)
    addr_id = models.IntegerField()
    balance = models.FloatField()
    last_ip = models.CharField(max_length=255)
    last_time = models.IntegerField()
    status = models.IntegerField()
    type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'szc_members'


class SzcModule(models.Model):
    id = models.AutoField(primary_key=True)  # AutoField?
    active = models.CharField(max_length=200)
    name = models.CharField(max_length=20)
    level = models.IntegerField()
    status = models.IntegerField(blank=True, null=True)
    iconfont = models.CharField(max_length=10, blank=True)

    class Meta:
        managed = False
        db_table = 'szc_module'





class SzcOrders(models.Model):
    id = models.AutoField(primary_key=True)  # AutoField?
    sn = models.CharField(max_length=17)
    uid = models.IntegerField()
    uname = models.CharField(max_length=50)
    tel = models.CharField(max_length=20,verbose_name=u'联系方式')
    addr = models.CharField(max_length=255)
    addrid = models.IntegerField(blank=True, null=True)
    couponid = models.IntegerField(blank=True, null=True)
    price = models.FloatField()
    paied = models.FloatField()
    order_time = models.IntegerField()
    pay_time = models.IntegerField(blank=True, null=True)
    pay_channel = models.CharField(max_length=10, blank=True)
    isnew = models.IntegerField()
    status = models.IntegerField()
    note = models.TextField(blank=True)
    district = models.CharField(max_length=12, blank=True)
    from_field = models.IntegerField(db_column='from')  # Field renamed because it was a Python reserved word.
    order_freight = models.FloatField()
    def __unicode__(self):
        return self.uname
    def currStatus(self):
        return u'已支付' if self.status==1 else u'未支付'
    currStatus.short_description=u'支付状态'
    currStatus.admin_order_field='status'
    class Meta:
        managed = False
        db_table = 'szc_orders'
        verbose_name="订单列表"

class SzcOrderDetail(models.Model):
    id = models.AutoField(primary_key=True)  # AutoField?
    order_id = models.ForeignKey(SzcOrders,db_column='order_id',verbose_name='订单id')
    dish_id = models.IntegerField()
    title = models.CharField(max_length=255,verbose_name='菜品名称')
    price = models.FloatField('菜品价格')
    count = models.IntegerField('菜品数量')
    def __unicode__(self):
        return self.title
    class Meta:
        managed = False
        db_table = 'szc_order_detail'
        verbose_name=u'订单详情'


class SzcPowers(models.Model):
    id = models.AutoField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=50, blank=True)
    lower = models.TextField(blank=True)
    status = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'szc_powers'


class SzcRechargeRecord(models.Model):
    id = models.AutoField(primary_key=True)  # AutoField?
    recharge_sn = models.CharField(max_length=20)
    member_id = models.IntegerField()
    value = models.IntegerField()
    create_time = models.CharField(max_length=11)
    end_time = models.CharField(max_length=11)
    status = models.IntegerField()
    pay_channel = models.CharField(max_length=5, blank=True)
    paid = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'szc_recharge_record'


class SzcRechargeType(models.Model):
    id = models.AutoField(primary_key=True)  # AutoField?
    value = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'szc_recharge_type'


class SzcStyle(models.Model):
    id = models.AutoField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=255, blank=True)
    benable = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'szc_style'


class SzcUser(models.Model):
    id = models.AutoField(primary_key=True)  # AutoField?
    uname = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50, blank=True)
    pwd = models.CharField(max_length=50)
    email = models.CharField(max_length=50, blank=True)
    tel = models.BigIntegerField(blank=True, null=True)
    area_name = models.CharField(max_length=20, blank=True)
    area_id = models.CharField(max_length=20, blank=True)
    group_id = models.IntegerField()
    pid = models.IntegerField()
    sid = models.IntegerField()
    last_ip = models.CharField(max_length=20, blank=True)
    last_time = models.IntegerField(blank=True, null=True)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'szc_user'


class SzcZone(models.Model):
    id = models.AutoField(primary_key=True)  # AutoField?
    zone_id = models.IntegerField(blank=True, null=True)
    zone_name = models.CharField(max_length=50, blank=True)
    level = models.IntegerField(blank=True, null=True)
    end = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'szc_zone'


