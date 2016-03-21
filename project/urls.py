from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'(?P<numero1>\d+)\+(?P<numero2>\d+)', 'calc.views.suma'),
    url(r'(?P<numero1>\d+)-(?P<numero2>\d+)', 'calc.views.resta'),
    url(r'(?P<numero1>\d+)\*(?P<numero2>\d+)', 'calc.views.multip'),
    url(r'(?P<numero1>\d+)\/(?P<numero2>\d+)', 'calc.views.division'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'.*', 'calc.views.error'),
)
