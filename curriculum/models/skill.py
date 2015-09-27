from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible
from curriculum.models import utils

SKILL_LEVELS = (
    (None, _('unknown')),
    ('B', _('beginner')),
    ('S', _('skilled')),
    ('A', _('advanced')),
    ('E', _('expert')),
)


@python_2_unicode_compatible
class Skill(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name=_("name"))
    description = models.TextField(max_length=2000, blank=True, verbose_name=_("description"))
    url = models.URLField(max_length=300, blank=True, verbose_name=_("URL"))
    tags = models.CharField(max_length=500, blank=True, verbose_name=_("tags"))
    color = models.CharField(max_length=50, blank=True, verbose_name=_("color"))

    class Meta:
        app_label = 'curriculum'
        ordering = ('name',)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class SkillItem(models.Model):
    resume = models.ForeignKey("curriculum.Resume", related_name='skills')

    skill = models.ForeignKey('curriculum.Skill', related_name='items')
    level = models.CharField(max_length=1, choices=SKILL_LEVELS, verbose_name=_("level"))
    category = models.CharField(max_length=50, blank=True, verbose_name=_("category"))

    start_year = models.IntegerField(choices=utils.YEARS, default=utils.current_year, null=True, blank=True, verbose_name=_("start year"))
    start_month = models.IntegerField(choices=utils.MONTHS, default=utils.current_month, null=True, blank=True, verbose_name=_("start month"))

    weight = models.IntegerField(choices=utils.WEIGHTS, default=1, verbose_name=_("weight"))

    class Meta:
        app_label = 'curriculum'
        unique_together = ('skill', 'resume')

    def __str__(self):
        return self.skill.name
