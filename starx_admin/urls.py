
from django.conf import settings
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from django.views.generic import RedirectView


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'starx_admin.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^accounts/', include('allauth.urls')),
    url(r'^mit_accounts/', include('mit_accounts.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^dashboard/', include('dashboard.urls')),
    url(r'^/dashboard/', include('dashboard.urls')),
    url(r'^/lti/', include('ims_lti.urls')),
    url(r'^lti/', include('ims_lti.urls')),
#    (r'^$', RedirectView.as_view(url='/dashboard/')),
)


if settings.DEBUG_TOOLBAR:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )
