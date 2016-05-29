#coding:utf-8
from django.contrib import admin
from szc.models import *
from django_admin_bootstrapped.admin.models import SortableInline

# Register your models here.

class OrderDetailLine(admin.TabularInline,SortableInline):
    model = SzcOrderDetail
    extra=0

@admin.register(SzcOrders)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderDetailLine]#内联一对多
    list_per_page = 5#每页显示数量
    list_display = ['id','sn','uname','tel','price','addr','currStatus']#概览显示数量
    # list_display_links=None


@admin.register(SzcOrderDetail)
class OrderdetailAdmin(admin.ModelAdmin):
    list_display=['id','title','price','count']
    list_per_page = 10
    fieldsets = [('详情',{'fields':['title','count']}),('价格',{'fields':['price']})]#详情页展示信息
    # 添加右边过滤
    list_filter = ['dish_id']
    # 顶部搜索栏
    search_fields = ['title']
    pass