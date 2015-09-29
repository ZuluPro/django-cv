"""
Template's tags and filters used for ease template usage.
"""
import re
from django import template
from django.utils.translation import ugettext_lazy as _
from ..models.utils import MONTHS

LETTER_MONTHS = dict(MONTHS)
URL_REGEX = re.compile(r'https?://([^/]*).*$')

register = template.Library()


@register.simple_tag
def daterange_display(start_year, start_month=None, end_year=None,
                      end_month=None):
    """
    Easily display a date range or date.
    """
    if not start_year:
        return ''
    if not start_month:
        if end_year:
            return _("%(start_year)i to %(end_year)i") % \
                    {'end_year': end_year, 'start_year': start_year}
        return start_year
    if end_year:
        if end_month:
            return _("%(start_month)s %(start_year)i to %(end_month)s %(end_year)i") % \
                    {'start_month': LETTER_MONTHS[start_month].capitalize(),
                     'start_year': start_year,
                     'end_month': LETTER_MONTHS[end_month].capitalize(),
                     'end_year': end_year}
        return _("%(start_year)s to %(end_year)i") % \
                {'start_year': start_year,
                 'end_year': end_year}
    if start_year and start_month:
        return _("%(start_month)s %(start_year)i") % \
                {'start_year': start_year, 'start_month': LETTER_MONTHS[start_month].capitalize()}


@register.filter
def shortlink(value, text=''):
    """
    Easily convert an URL into a HTML a tag.
    """
    if not value:
        return text
    text = text or URL_REGEX.sub(r'\1', value)
    return '<a href="%s">%s</a>' % (value, text)
