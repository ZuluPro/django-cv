"""
Views that can used by developer for easily export resume as PDF.
"""
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from curriculum import export
from curriculum.models import Resume


def export_single_page(request, resume_id):
    """Get a resume in a single page PDF."""
    resume = get_object_or_404(Resume.objects.filter(id=resume_id))
    pdf, result = export.export_pdf(resume, export.single_page)
    raw_pdf = result.getvalue()
    if not pdf.err:
        return HttpResponse(raw_pdf, content_type='application/pdf')
    return HttpResponse('We had some errors.')


def export_classic(request, resume_id):
    """Get a resume in a PDF with classic format."""
    resume = get_object_or_404(Resume.objects.filter(id=resume_id))
    pdf, result = export.export_pdf(resume, export.classic)
    raw_pdf = result.getvalue()
    if not pdf.err:
        return HttpResponse(raw_pdf, content_type='application/pdf')
    return HttpResponse('We had some errors.')
