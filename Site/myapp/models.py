#coding:utf-8
from django.db import models

# Create your models here.
# class MemberType(models.Model):
#     id=models.AutoField(primary_key=True,unique=True)
#     typename=models.CharField(blank=False,null=False,max_length=5)
#     status=models.BooleanField(default=True)
#     createtime=models.DateTimeField(auto_now_add=True,editable=True)
#     updatetime=models.TimeField(auto_now_add=True,auto_now=True)
#     def __unicode__(self):
#         return self.typename
# class Member(models.Model):
#     id=models.AutoField(primary_key=True,unique=True,auto_created=True,blank=False,null=False,help_text=u'主键id')
#     name=models.CharField(max_length=5,help_text=u'会员姓名')
#     tel=models.CharField(max_length=11,help_text=u'会员手机号')
#     account=models.FloatField(default=0.0,help_text=u'账户余额',verbose_name=u'可是对方')
#     member_type=models.ForeignKey(MemberType)
#     def __unicode__(self):
#         return self.name

