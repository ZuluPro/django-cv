import os
from django.conf import settings
from django.template import Context
from django.template.loader import get_template
from django.utils.six import StringIO
import xhtml2pdf.pisa as pisa


def single_page(resume):
    context = Context({
        'pagesize': 'a4',
        'resume': resume,
        'skills': resume.skills.filter(weight=2),
        'projects': resume.projects.filter(weight__gte=1).order_by('-weight'),
        'experiences': resume.experiences.filter(weight__gte=1),
        'trainings': resume.trainings.order_by('-year', '-month'),
        'certifications': resume.certifications.order_by('-start_year', '-start_month')
    })
    return get_template('curriculum/single_page.html').render(context)


def classic(resume):
    context = Context({
        'pagesize': 'a4',
        'resume': resume,
        'skills': resume.skills.order_by('category', '-weight'),
        'projects': resume.projects.order_by('-weight'),
        'experiences': resume.experiences.order_by('-start_year'),
        'trainings': resume.trainings.order_by('-year', '-month'),
        'certifications': resume.certifications.order_by('-start_year', '-start_month')
    })
    return get_template('curriculum/classic.html').render(context)


def custom_classic(resume, skills=None, projects=None, experiences=None,
                   trainings=None, certifications=None, **options):
    if skills is None:
        skills = resume.skills.all()
    skills = skills.order_by('category', '-weight')
    if projects is None:
        projects = resume.projects.all()
    projects = projects.order_by('-weight')
    if experiences is None:
        experiences = resume.experiences.all()
    experiences = experiences.order_by('-start_year')
    if trainings is None:
        trainings = resume.trainings.all()
    trainings = trainings.order_by('-year', '-month')
    if certifications is None:
        certifications = resume.certifications.all()
    certifications = certifications.order_by('-start_year', '-start_month')

    context_dict = {
        'pagesize': 'a4',
        'resume': resume,
        'skills': skills,
        'projects': projects,
        'experiences': experiences,
        'trainings': trainings,
        'certifications': certifications
    }
    context_dict.update(options)
    context = Context(context_dict)
    return get_template('curriculum/classic.html').render(context)


def export_pdf(resume, resume_func, resume_func_kwargs=None):
    resume_func_kwargs = resume_func_kwargs or {}
    html = resume_func(resume, **resume_func_kwargs)
    result = StringIO()
    pdf = pisa.pisaDocument(
        StringIO(html.encode("UTF-8")),
        dest=result,
        encoding='UTF-8',
        link_callback=fetch_resources)
    return pdf, result


def fetch_resources(uri, rel):
    if uri.startswith(settings.STATIC_URL):
        path = os.path.join(
            settings.STATIC_ROOT,
            uri.replace(settings.STATIC_URL, ""))
    elif uri.startswith(settings.MEDIA_URL):
        path = os.path.join(
            settings.MEDIA_ROOT,
            uri.replace(settings.MEDIA_URL, ""))
    else:
        path = ''
    return path
