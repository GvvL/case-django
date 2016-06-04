from django.contrib import admin
from models import *
import forms


@admin.register(SzcOrders)
class OrderAdmin(admin.ModelAdmin):
    form = forms.OrderForm
    list_display = ['id','uname','tel','pay_time','status','pay_channel']
    list_filter = ['status','pay_channel']
    search_fields = ('aa',list_display)
    pass



@admin.register(SzcAddr)
class AddrAdmin(admin.ModelAdmin):

    pass

@admin.register(SzcCoupons)
class CouponsAdmin(admin.ModelAdmin):
    pass

@admin.register(SzcMembers)
class MemeberAdmin(admin.ModelAdmin):
    pass

