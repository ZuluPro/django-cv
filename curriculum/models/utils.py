"""Utilities for Curriculum's models."""
from django.utils.translation import ugettext_lazy as _

YEARS = [(i, i) for i in range(1900, 2100)]
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
