from django.test import TestCase
from django.core.urlresolvers import reverse
from curriculum.tests import factories


class RevealJSTest(TestCase):
    def test_view(self):
        resume = factories.ResumeFactory()
        url = reverse('reveal-js', args=[resume.id])
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
