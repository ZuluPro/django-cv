from django.shortcuts import render, get_object_or_404
from curriculum.models import Resume


def get_resume(request, resume_id):
    resume = get_object_or_404(Resume.objects.filter(id=resume_id))
    return render(request, 'revealjs.html', {
        'resume': resume,
        'skills': resume.skills.order_by('category', '-weight'),
        'projects': resume.projects.order_by('-weight'),
        'experiences': resume.experiences.order_by('-start_year'),
        'trainings': resume.trainings.order_by('-year', '-month'),
        'certifications': resume.certifications.order_by('-start_year', '-start_month')
    })
