from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'my_blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'article.views.home', name='home'),
    url(r'^(?P<id>\d+)/$', 'article.views.detail', name='detail'),
    url(r'^index$', 'test01.views.index', name='index'),
    url(r'^test01$', 'test01.views.test01'),
    url(r'^test02$', 'test01.views.test02',),
    url(r'^add/$', 'test01.views.add', name='add'),
    url(r'^ajax_list/$', 'test01.views.ajax_list', name='ajax-list'),
    url(r'^ajax_dict/$', 'test01.views.ajax_dict', name='ajax-dict'),
)
