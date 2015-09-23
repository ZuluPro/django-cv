from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible

LANGUAGE_LEVELS = (
    ('NOT', _("Notion")),
    ('BAS', _('basic')),
    ('ADV', _('advanced')),
    ('PRO', _('professional')),
    ('BIL', _('bilingual')),
)


@python_2_unicode_compatible
class Language(models.Model):
    name = models.CharField(max_length=50, primary_key=True, unique=True, verbose_name=_("name"))
    description = models.TextField(max_length=2000, blank=True, verbose_name=_("description"))

    class Meta:
        app_label = 'curriculum'
        ordering = ('name',)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class LanguageItem(models.Model):
    resume = models.ForeignKey("curriculum.Resume", related_name='languages')

    language = models.ForeignKey('curriculum.Language', 'name', related_name='items')
    level = models.CharField(max_length=5, choices=LANGUAGE_LEVELS, default=LANGUAGE_LEVELS[0][0], verbose_name=_('level'))

    class Meta:
        app_label = 'curriculum'
        unique_together = ('language', 'resume')

    def __str__(self):
        return self.language.name
