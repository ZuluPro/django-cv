from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from curriculum.tests import factories

User = get_user_model()


class AdminExportResumeTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='Mike', is_superuser=True, is_staff=True)
        self.user.set_password('foo')
        self.user.save()
        self.client.login(username='Mike', password='foo')

    def test_get(self):
        resume = factories.ResumeFactory()
        url = reverse('admin:curriculum_resume_changelist')
        data = {
            '_selected_action': [resume.id],
            'action': 'export_resume',
            'index': '0',
            'select_across': '0',
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, resume.title)

    def test_export(self):
        resume = factories.ResumeFactory()
        url = reverse('admin:curriculum_resume_changelist')
        data = {
            '_export': '_export',
            '_selected_action': [resume.id],
            'action': ['export_resume'],
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
