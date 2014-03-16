# -*- coding: utf-8 -*-
from django.conf.urls import patterns,url, include

urlpatterns = patterns('home.views',
	url(r'^$','home'),
)
