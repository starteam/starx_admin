from django.conf.urls import url, patterns, include
from django.utils import importlib


urlpatterns = patterns('',
    url(r'^$', 'ims_lti.views.index', name='lti_index'),
    url(r'^/$', 'ims_lti.views.index', name='lti_index'),
    url(r'^add$', 'ims_lti.views.add_problem', name='AddProblem'),
)
