from django.conf.urls import patterns, include, url
from django.contrib import admin
from myapp import views as myapp

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'Site.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^index$', myapp.index, name='indexname'),
                       url(r'^add$', myapp.add, name='addname'),
                       url(r'^add2/(\d+)/(\d+)$',myapp.add2,name='add2name'),
                       url(r'^home$',myapp.home,name='homename')
                       )
