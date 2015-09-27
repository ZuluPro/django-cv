import os
from django.conf import settings
from django.template import Context
from django.template.loader import get_template
from django.utils.six import StringIO
import xhtml2pdf.pisa as pisa


def single_page(resume):
    context = Context({
        'resume': resume,
        'skills': resume.skills.filter(weight=2),
        'projects': resume.projects.filter(weight__gte=1).order_by('-weight'),
        'experiences': resume.experiences.filter(weight__gte=1),
        'trainings': resume.trainings.order_by('-year', '-month'),
        'certifications': resume.certifications.order_by('-start_year', '-start_month')
    })
    page = get_template('single_page.html').render(context)
    return [page]


def classic(resume):
    context = Context({
        'resume': resume,
        'skills': resume.skills.order_by('category', '-weight'),
        'projects': resume.projects.order_by('-weight'),
        'experiences': resume.experiences.order_by('-start_year'),
        'trainings': resume.trainings.order_by('-year', '-month'),
        'certifications': resume.certifications.order_by('-start_year', '-start_month')
    })
    page = get_template('classic.html').render(context)
    return [page]


def export_pdf(resume, resume_func):
    template = get_template('base_pdf.html')
    context = Context({
        'pagesize': 'a4',
        'title': 'Resume',
        'introduction': '',
        'pages': resume_func(resume)
    })
    html = template.render(context)
    result = StringIO()
    pdf = pisa.pisaDocument(
        StringIO(html.encode("UTF-8")),
        dest=result,
        encoding='UTF-8',
        link_callback=fetch_resources)
    return pdf, result


def fetch_resources(uri, rel):
    if uri.startswith('/tmp/'):
        path = uri
    elif uri.startswith(settings.STATIC_URL):
        path = os.path.join(
            settings.STATIC_ROOT,
            uri.replace(settings.STATIC_URL, ""))
    elif uri.startswith(settings.MEDIA_URL):
        path = os.path.join(
            settings.MEDIA_ROOT,
            uri.replace(settings.MEDIA_URL, ""))
    return path
