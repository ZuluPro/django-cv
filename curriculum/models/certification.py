from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Certification(models.Model):
    title = models.CharField(max_length=50, verbose_name=_("title"))
    authority = models.CharField(max_length=200, verbose_name=_("authority"))
    url = models.URLField(max_length=300, blank=True, verbose_name=_("url"))
    description = models.TextField(max_length=2000, blank=True, verbose_name=_("description"))

    class Meta:
        app_label = 'curriculum'
        unique_together = ('title', 'authority')

    def __str__(self):
        return _('%(title)s at %(authority)s') % \
                {'title': self.title, 'authority': self.authority}


@python_2_unicode_compatible
class CertificationItem(models.Model):
    certification = models.ForeignKey("curriculum.Certification", related_name='items')
    resume = models.ForeignKey("curriculum.Resume", related_name='certifications')

    start_year = models.IntegerField(verbose_name=_("start year"))
    start_month = models.IntegerField(verbose_name=_("start month"))
    expires = models.BooleanField(default=False, verbose_name=_("expires"))
    end_year = models.IntegerField(null=True, blank=True, verbose_name=_("end year"))
    end_month = models.IntegerField(null=True, blank=True, verbose_name=_("end month"))

    class Meta:
        app_label = 'curriculum'
        unique_together = ('certification', 'resume')

    def __str__(self):
        return _('%(title)s at %(authority)s') % \
                {'title': self.certification.title, 'authority': self.certification.authority}
