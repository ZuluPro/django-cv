from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static


urlpatterns = patterns(
    '',
    url(r'^revealjs/(?P<resume_id>\d*)/$', 'curriculum.revealjs.views.get_resume', name="reveal-js"),
    url(r'^export/(?P<resume_id>\d*)/single_page', 'curriculum.views.export_single_page', name="single_page"),
    url(r'^export/(?P<resume_id>\d*)(!/classic)?', 'curriculum.views.export_classic', name="classic"),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
