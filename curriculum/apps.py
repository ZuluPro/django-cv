"""Apps for Curriculum"""
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class CurriculumConfig(AppConfig):
    """Config for Curriculum application."""
    name = 'curriculum'
    label = 'curriculum'
    verbose_name = _('Curriculum')
