from unittest.mock import patch, Mock
from django.contrib.auth import get_user_model
from django.http import HttpRequest
from django.test import TestCase
from django.utils.html import escape
from resume.forms import ResumeForm
from resume.models import Resume


class NewResumePageTest(TestCase):

    def test_uses_new_resume_template(self):
        response = self.client.get('/resume')
        self.assertTemplateUsed(response, 'new_resume.html')


    def test_home_page_uses_item_form(self):
        response = self.client.get('/resume')
        self.assertIsInstance(response.context['form'], ResumeForm)



class NewResumeViewIntegratedTest(TestCase):

    def test_can_save_a_POST_request(self):
        self.client.post('/resume', data={'display_name': 'Alex Walder', 'date_of_birth': '16/11/1998', 'phone_number': '07452842381', 'email':'alex.walder9@gmail.com', 'personal_summary': 'This is a test personal summary.'})
        self.assertEqual(Resume.objects.count(), 1)
        new_resume = Resume.objects.first()
        self.assertEqual(new_resume.display_name, 'Alex Walder')



class ResumeViewTest(TestCase):

    def test_uses_resume_template(self):
        self.client.post('/resume', data={'display_name': 'Alex Walder', 'date_of_birth': '16/11/1998', 'phone_number': '07452842381', 'email':'alex.walder9@gmail.com', 'personal_summary': 'This is a test personal summary.'})
        resume = Resume.objects.get(id=1)
        response = self.client.get(f'/resume/{resume.id}')
        self.assertTemplateUsed(response, 'view_resume.html')


    def test_passes_correct_resume_to_template(self):
        self.client.post('/resume', data={'display_name': 'Alex Walder', 'date_of_birth': '16/11/1998', 'phone_number': '07452842381', 'email':'alex.walder9@gmail.com', 'personal_summary': 'This is a test personal summary.'})
        correct_resume = Resume.objects.get(id=1)
        response = self.client.get(f'/resume/{correct_resume.id}')
        self.assertEqual(response.context['cv'], correct_resume)



class ItemModelTest(TestCase):

    def test_default_text(self):
        resume = Resume()
        self.assertEqual(resume.display_name, '')
