from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible
from curriculum.models import utils


@python_2_unicode_compatible
class Project(models.Model):
    title = models.CharField(max_length=200, unique=True, verbose_name=_("title"))
    description = models.TextField(max_length=3000, blank=True, verbose_name=_("description"))
    url = models.URLField(max_length=300, blank=True, verbose_name=_("URL"))

    class Meta:
        app_label = 'curriculum'

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class ProjectItem(models.Model):
    resume = models.ForeignKey("curriculum.Resume", related_name='projects')
    project = models.ForeignKey("curriculum.Project", related_name='items')
    contribution = models.TextField(max_length=3000, blank=True, verbose_name=_("contribution"))

    start_year = models.IntegerField(choices=utils.YEARS, default=utils.current_year, verbose_name=_("start year"))
    start_month = models.IntegerField(choices=utils.MONTHS, default=utils.current_month, verbose_name=_("start month"))
    still = models.BooleanField(default=True, verbose_name=_("still contributor"))
    end_year = models.IntegerField(choices=utils.YEARS, null=True, blank=True, verbose_name=_("end year"))
    end_month = models.IntegerField(choices=utils.MONTHS, null=True, blank=True, verbose_name=_("end month"))

    weight = models.IntegerField(choices=utils.WEIGHTS, default=1, verbose_name=_("weight"))

    class Meta:
        app_label = 'curriculum'
        unique_together = ('resume', 'project')

    def __str__(self):
        return self.project.title
