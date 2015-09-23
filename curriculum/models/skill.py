from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible

SKILL_LEVELS = [(c, c) for c in 'ABCDED']


@python_2_unicode_compatible
class Skill(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name=_("name"))
    description = models.TextField(max_length=2000, blank=True, verbose_name=_("description"))

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

    class Meta:
        app_label = 'curriculum'
        unique_together = ('skill', 'resume')

    def __str__(self):
        return self.skill.name
