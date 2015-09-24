from django.template import Context
from django.template.loader import get_template


def single_page(resume):
    context = Context({'resume': resume})
    page = get_template('single_page.html').render(context)
    return [page]
