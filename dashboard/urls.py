from django.conf.urls import url, patterns, include
from django.utils import importlib

urlpatterns = patterns('',
    url(r'^$', 'dashboard.views.index', name='home'),
)