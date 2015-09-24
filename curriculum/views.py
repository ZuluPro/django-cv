import os
import cgi

from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import get_object_or_404
from django.utils.six import StringIO
from django.conf import settings

import xhtml2pdf.pisa as pisa

from curriculum import export
from curriculum.models import Resume


def export_resume(request, resume_id):
    resume = get_object_or_404(Resume.objects.filter(id=resume_id))
    template = get_template('base_pdf.html')
    context = Context({
        'pagesize': 'a4',
        'title': 'Resume',
        'introduction': '',
        'pages': export.single_page(resume)
    })
    html = template.render(context)
    result = StringIO()
    pdf = pisa.pisaDocument(
        StringIO(html.encode("UTF-8")),
        dest=result,
        encoding='UTF-8',
        link_callback=fetch_resources
    )
    raw_pdf = result.getvalue()
    if not pdf.err:
        return HttpResponse(raw_pdf, content_type='application/pdf')
    return HttpResponse('We had some errors<pre>%s</pre>' % cgi.escape(html))


def fetch_resources(uri, rel):
    if uri.startswith('/tmp/'):
        path = uri
    else:
        path = os.path.join(
            settings.STATIC_ROOT,
            uri.replace(settings.STATIC_URL, ""))
    return path
