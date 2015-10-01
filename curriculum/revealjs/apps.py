"""Apps for Curriculum"""
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class CurriculumRevealJsConfig(AppConfig):
    """Config for Curriculum application."""
    name = 'curriculum.revealjs'
    label = 'curriculum_revealjs'
    verbose_name = _('Curriculum Reveal.JS')
