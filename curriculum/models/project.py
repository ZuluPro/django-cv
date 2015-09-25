from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible
from curriculum.models.utils import YEARS, MONTHS


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

    start_year = models.IntegerField(choices=YEARS, verbose_name=_("start year"))
    start_month = models.IntegerField(choices=MONTHS, verbose_name=_("start month"))
    still = models.BooleanField(default=True, verbose_name=_("still contributor"))
    end_year = models.IntegerField(choices=YEARS, null=True, blank=True, verbose_name=_("end year"))
    end_month = models.IntegerField(choices=MONTHS, null=True, blank=True, verbose_name=_("end month"))

    class Meta:
        app_label = 'curriculum'
        unique_together = ('resume', 'project')

    def __str__(self):
        return self.project.title
