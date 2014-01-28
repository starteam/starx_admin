from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from django.views.generic import RedirectView


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'starx_admin.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^dashboard/', include('dashboard.urls')),
    url(r'^accounts/', include('allauth.urls')),
    (r'^$', RedirectView.as_view(url='/dashboard/')),

)
