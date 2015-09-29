from django.test import TestCase
from curriculum import export
from curriculum.tests import factories

MEDIA_IMAGE_URL = '/media/avatar.png'
STATIC_IMAGE_URL = '/static/yeswecode.jpg'


class ExportSinglePageTest(TestCase):
    def test_basic(self):
        resume = factories.ResumeFactory()
        export.single_page(resume)

    def test_with_image(self):
        resume = factories.ResumeFactory(image=MEDIA_IMAGE_URL)
        export.single_page(resume)


class ExportClassicTest(TestCase):
    def test_basic(self):
        resume = factories.ResumeFactory()
        export.classic(resume)

    def test_with_image(self):
        resume = factories.ResumeFactory(image=MEDIA_IMAGE_URL)
        export.single_page(resume)


class ExportCustomClassicTest(TestCase):
    def test_basic(self):
        resume = factories.ResumeFactory()
        export.custom_classic(resume)


class ExportPdfTest(TestCase):
    def test_func(self):
        resume = factories.ResumeFactory()
        pdf, result = export.export_pdf(resume, lambda x: x.__str__())
        raw_pdf = result.getvalue()
        self.assertFalse(pdf.err)


class FetchRessourcesTest(TestCase):
    def test_media(self):
        path = export.fetch_resources(MEDIA_IMAGE_URL, '')
        self.assertTrue(path.endswith('avatar.png'))

    def test_static(self):
        path = export.fetch_resources(STATIC_IMAGE_URL, '')
        self.assertTrue(path.endswith('yeswecode.jpg'))

    def test_unfound(self):
        path = export.fetch_resources('BAD_URL', '')
        self.assertEqual(path, '')
