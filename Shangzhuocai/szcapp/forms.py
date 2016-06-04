#coding:utf-8
from django.forms import ModelForm
from suit.widgets import *
from models import SzcOrders
class OrderForm(ModelForm):
    class Meta:
        widgets = {

            # You can also use prepended and appended together
            'price': EnclosedInput(prepend=u'¥', append=u'元',attrs={'class': 'input-mini'}),
            'paied': EnclosedInput(prepend=u'¥', append=u'元',attrs={'class': 'input-mini'}),
            'pay_time': SuitSplitDateTimeWidget,
            # Use HTML for append/prepend (See Twitter Bootstrap docs of supported tags)
            # 'url': EnclosedInput(prepend='icon-home', append='<input type="button" class="btn"  value="Open link">'),

        }