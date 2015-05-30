from django.conf.urls import patterns, include, url
from django.contrib import admin
from filebrowser.sites import site
from django.views.generic.base import TemplateView
import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'web.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/templates/', include('grappelli_te.urls')),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^$', TemplateView.as_view(template_name="index.html")),
    url(r'^$', 'webapp.views.home', name='home'),
    url(r"^account/", include("account.urls")),
    url(r'^profile/$', 'webapp.views.profile', name='profile'),


)

if settings.DEBUG :
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT, 'show_indexes': True}),
    )