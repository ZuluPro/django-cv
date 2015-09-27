from django.test import TestCase
from django.core.urlresolvers import reverse
from curriculum.tests import factories


class ViewExportSinglePage(TestCase):
    def test_view(self):
        resume = factories.ResumeFactory()
        url = reverse('single_page', args=[resume.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


class ViewExportClassic(TestCase):
    def test_view(self):
        resume = factories.ResumeFactory()
        url = reverse('classic', args=[resume.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
