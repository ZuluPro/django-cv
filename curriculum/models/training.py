from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Training(models.Model):
    resume = models.ForeignKey("curriculum.Resume", related_name='trainings')

    school = models.CharField(max_length=150, verbose_name=_("school"))
    degree = models.CharField(max_length=150, verbose_name=_("degree"))
    topic = models.CharField(max_length=150, blank=True, verbose_name=_("topic"))
    result = models.CharField(max_length=150, blank=True, verbose_name=_("result"))
    description = models.TextField(max_length=3000, blank=True, verbose_name=_("description"))

    year = models.IntegerField(verbose_name=_("year"))
    month = models.IntegerField(verbose_name=_("month"))

    class Meta:
        app_label = 'curriculum'

    def __str__(self):
        return self.degree
