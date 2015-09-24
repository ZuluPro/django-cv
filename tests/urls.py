from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns(
    '',
    url(r'^export/(?P<resume_id>\d*)', 'curriculum.views.export_resume', name="export_resume"),
    url(r'^admin/', include(admin.site.urls)),
)
