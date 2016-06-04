#coding:utf-8
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models
from django_unixdatetimefield import UnixDateTimeField


class SzcAddr(models.Model):
    member_id = models.IntegerField(verbose_name='add序号ID')
    address_linkman = models.CharField(max_length=5)
    address_linktel = models.CharField(max_length=11, blank=True, null=True)
    address_detail = models.CharField(max_length=30)
    status = models.IntegerField()
    isdefault = models.IntegerField()

    def __unicode__(self):
        return self.address_detail
    class Meta:
        managed = False
        db_table = 'szc_addr'
        verbose_name='地址'


class SzcBannerType(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'szc_banner_type'


class SzcBanners(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True)
    typeid = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    img = models.CharField(max_length=255, blank=True, null=True)

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
    id=models.AutoField(primary_key=True,unique=True,verbose_name='序号ID')
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
    id=models.AutoField(primary_key=True,unique=True,verbose_name='序号ID')
    uid = models.IntegerField()
    value = models.FloatField()
    min = models.FloatField()
    valid_date = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'szc_coupons'


class SzcDishTypes(models.Model):
    id=models.AutoField(primary_key=True,unique=True,verbose_name='序号ID')
    title = models.CharField(max_length=20)
    benable = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'szc_dish_types'


class SzcDishes(models.Model):
    id=models.AutoField(primary_key=True,unique=True,verbose_name='序号ID')
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
    id=models.AutoField(primary_key=True,unique=True,verbose_name='序号ID')
    name = models.CharField(max_length=50)
    lower = models.CharField(max_length=2000)
    status = models.IntegerField()
    description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'szc_group'


class SzcMemberAddress(models.Model):
    id=models.AutoField(primary_key=True,unique=True,verbose_name='序号ID')
    uid = models.IntegerField()
    uname = models.CharField(max_length=50)
    tel = models.CharField(max_length=20)
    addr = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'szc_member_address'


class SzcMembers(models.Model):
    id=models.AutoField(primary_key=True,unique=True)
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
    id=models.AutoField(primary_key=True,unique=True)
    active = models.CharField(max_length=200)
    name = models.CharField(max_length=20)
    level = models.IntegerField()
    status = models.IntegerField(blank=True, null=True)
    iconfont = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'szc_module'


class SzcOrderDetail(models.Model):
    id=models.AutoField(primary_key=True,unique=True)
    order_id = models.IntegerField()
    dish_id = models.IntegerField()
    title = models.CharField(max_length=255)
    price = models.FloatField()
    count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'szc_order_detail'

class SzcOrders(models.Model):
    id=models.AutoField(u'订单id',primary_key=True,unique=True)
    sn = models.CharField(max_length=17)
    uid = models.IntegerField()
    uname = models.CharField(u'联系人',max_length=50)
    tel = models.CharField(u'联系电话',max_length=20)
    addr = models.CharField(max_length=255)
    addrid = models.IntegerField(blank=True, null=True)
    couponid = models.IntegerField(blank=True, null=True)
    price = models.FloatField()
    paied = models.FloatField()
    order_time = models.IntegerField()
    # pay_time=models.BigIntegerField(u'支付时间',blank=True, null=True)
    pay_time=UnixDateTimeField(u'支付时间',blank=True,null=True)
    CHANNEL_CHOICES=(('wx','微信'),('alipay','支付宝'),('yue','余额'),('','未知'))
    pay_channel = models.CharField(u'支付渠道',max_length=10, blank=True, null=True,choices=CHANNEL_CHOICES)
    isnew = models.IntegerField()
    STATUS_CHOICES=((1,'已支付'),(2,'已退款'),(0,'待支付'))
    status = models.IntegerField(choices=STATUS_CHOICES,default=0,verbose_name='订单状态')
    note = models.TextField(blank=True, null=True)
    district = models.CharField(max_length=12, blank=True, null=True)
    from_field = models.IntegerField(db_column='from')  # Field renamed because it was a Python reserved word.
    order_freight = models.FloatField()


    class Meta:
        managed = False
        db_table = 'szc_orders'
        verbose_name='订单列表'




class SzcPowers(models.Model):
    id=models.AutoField(primary_key=True,unique=True,verbose_name='序号ID')
    name = models.CharField(max_length=50, blank=True, null=True)
    lower = models.TextField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'szc_powers'


class SzcRechargeRecord(models.Model):
    id=models.AutoField(primary_key=True,unique=True,verbose_name='序号ID')
    recharge_sn = models.CharField(max_length=20)
    member_id = models.IntegerField()
    value = models.IntegerField()
    create_time = models.CharField(max_length=11)
    end_time = models.CharField(max_length=11)
    status = models.IntegerField()
    pay_channel = models.CharField(max_length=5, blank=True, null=True)
    paid = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'szc_recharge_record'


class SzcRechargeType(models.Model):
    id=models.AutoField(primary_key=True,unique=True,verbose_name='序号ID')
    value = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'szc_recharge_type'


class SzcStyle(models.Model):
    id=models.AutoField(primary_key=True,unique=True,verbose_name='序号ID')
    name = models.CharField(max_length=255, blank=True, null=True)
    benable = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'szc_style'


class SzcUser(models.Model):
    id=models.AutoField(primary_key=True,unique=True,verbose_name='序号ID')
    uname = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50, blank=True, null=True)
    pwd = models.CharField(max_length=50)
    email = models.CharField(max_length=50, blank=True, null=True)
    tel = models.BigIntegerField(blank=True, null=True)
    area_name = models.CharField(max_length=20, blank=True, null=True)
    area_id = models.CharField(max_length=20, blank=True, null=True)
    group_id = models.IntegerField()
    pid = models.IntegerField()
    sid = models.IntegerField()
    last_ip = models.CharField(max_length=20, blank=True, null=True)
    last_time = models.IntegerField(blank=True, null=True)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'szc_user'


class SzcZone(models.Model):
    id=models.AutoField(primary_key=True,unique=True,verbose_name='序号ID')
    zone_id = models.IntegerField(blank=True, null=True)
    zone_name = models.CharField(max_length=50, blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)
    end = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'szc_zone'
