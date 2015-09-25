from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible
# from curriculum.models.utils import YEARS, MONTHS

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
    # url = models.URLField(max_length=300, blank=True, verbose_name=_("URL"))

    class Meta:
        app_label = 'curriculum'
        ordering = ('name',)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class SkillItem(models.Model):
    resume = models.ForeignKey("curriculum.Resume", related_name='skills')

    skill = models.ForeignKey('curriculum.Skill', 'name', related_name='items')
    level = models.CharField(max_length=1, choices=SKILL_LEVELS)

    # start_year = models.IntegerField(choices=YEARS, verbose_name=_("start year"))
    # start_month = models.IntegerField(choices=MONTHS, null=True, verbose_name=_("start month"))

    class Meta:
        app_label = 'curriculum'
        unique_together = ('skill', 'resume')

    def __str__(self):
        return self.skill.name
