from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible


EXPERIENCE_TYPES = (
    (None, _('unknown')),
    ('SALAR', _('salaried')),
    ('CHIEF', _('founder/chief')),
    ('FREEL', _('freelance/chief')),
    ('OTHER', _('other')),
)


@python_2_unicode_compatible
class Experience(models.Model):
    resume = models.ForeignKey("curriculum.Resume", related_name='experiences')

    title = models.CharField(max_length=200, verbose_name=_("title"))
    entreprise = models.CharField(max_length=200, verbose_name=_("entreprise"))
    description = models.TextField(max_length=3000, blank=True, verbose_name=_("description"))
    type = models.CharField(choices=EXPERIENCE_TYPES, max_length=5, null=True, verbose_name=_("type"))

    start_year = models.IntegerField(verbose_name=_("start year"))
    start_month = models.IntegerField(verbose_name=_("start month"))
    still = models.BooleanField(default=True, verbose_name=_("still in office"))
    end_year = models.IntegerField(null=True, blank=True, verbose_name=_("end year"))
    end_month = models.IntegerField(null=True, blank=True, verbose_name=_("end month"))

    def __str__(self):
        return _('%(title)s at %(entreprise)s') % \
                {'title': self.title, 'entreprise': self.entreprise}

    class Meta:
        app_label = 'curriculum'
