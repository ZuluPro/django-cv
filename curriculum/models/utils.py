"""Utilities for Curriculum's models."""
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import now

YEARS = [(i, i) for i in range(1900, 2030)][::-1]
MONTHS = (
    (1, _('january')),
    (2, _('febuary')),
    (3, _('march')),
    (4, _('april')),
    (5, _('may')),
    (6, _('june')),
    (7, _('july')),
    (8, _('august')),
    (9, _('september')),
    (10, _('october')),
    (11, _('november')),
    (12, _('december')),
)

WEIGHTS = (
    (0, _('Minor')),
    (1, _('Medium')),
    (2, _('Major')),
)


def current_year():
    return now().year


def current_month():
    return now().month
