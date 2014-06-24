from django.conf.urls import url, patterns, include
from django.utils import importlib

urlpatterns = patterns('',
    url(r'^$', 'mit_accounts.views.index', name='home'),
)
