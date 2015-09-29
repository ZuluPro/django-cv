"""
Admininistration site actions.
"""
from django.http import HttpResponse
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render, get_object_or_404

from curriculum import export
from curriculum.models import Resume
from curriculum.forms import ResumeExportForm


def export_resume(modeladmin, request, queryset):
    """
    Action in two steps:

    1. Display a form for ask which information will be included in document
    2. Export document with defined data
    """
    if '_export' not in request.POST:
        resume_ids = request.POST.getlist('_selected_action')
        resumes = Resume.objects.filter(id__in=resume_ids)
        formset = [ResumeExportForm(instance=resume) for resume in resumes]
        return render(request, 'curriculum/export.html', {
            'title': _("Export resume(s) as document"),
            'formset': formset,
            'opts': Resume._meta
        })
    else:
        resume_id = request.POST.get('_selected_action')
        resume = get_object_or_404(Resume.objects.filter(id=resume_id))
        resume.image = None if 'hide_image' in request.POST else resume.image
        resume.resume = None if 'hide_resume' in request.POST else resume.resume
        resume.phone = None if 'hide_phone' in request.POST else resume.phone
        resume.city = None if 'hide_city' in request.POST else resume.city
        resume.country = None if 'hide_country' in request.POST else resume.country
        resume.address = None if 'hide_address' in request.POST else resume.address
        resume.email = None if 'hide_email' in request.POST else resume.email
        resume.website = None if 'hide_website' in request.POST else resume.website
        resume.skype = None if 'hide_skype' in request.POST else resume.skype
        resume.twitter = None if 'hide_twitter' in request.POST else resume.twitter
        resume.linkedin = None if 'hide_linkedin' in request.POST else resume.linkedin
        resume.stackoverflow = None if 'hide_stackoverflow' in request.POST else resume.stackoverflow
        resume.github = None if 'hide_github' in request.POST else resume.github
        options = {
            'skills': resume.skills.filter(id__in=request.POST.getlist('skills')),
            'experiences': resume.experiences.filter(id__in=request.POST.getlist('experiences')),
            'trainings': resume.trainings.filter(id__in=request.POST.getlist('trainings')),
            'certifications': resume.certifications.filter(id__in=request.POST.getlist('certifications')),
            'projects': resume.projects.filter(id__in=request.POST.getlist('projects')),
            'hide_experience_description': request.POST.get('hide_experience_description', False),
            'hide_experience_environment': request.POST.get('hide_experience_environment', False),
            'hide_certification_description': request.POST.get('hide_certification_description', False),
            'hide_training_description': request.POST.get('hide_training_description', False),
            'hide_project_contribution': request.POST.get('hide_project_contribution', False),
            'hide_project_url': request.POST.get('hide_project_url', False)
        }
        pdf, result = export.export_pdf(resume, export.custom_classic, options)
        raw_pdf = result.getvalue()
        if not pdf.err:
            return HttpResponse(raw_pdf, content_type='application/pdf')
        return HttpResponse('We had some errors.')

export_resume.short_description = _("Export resume as document")
