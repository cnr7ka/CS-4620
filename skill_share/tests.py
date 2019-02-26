from django.test import TestCase
from skill_share.models import Skill, Student
from skill_share.forms import createAccountForm, createSkillForm
from skill_share.views import *
from django.http import HttpRequest

# Create your tests here.
class ProfilePageTest(TestCase):
  def test_profile_page_returns_html(self):
    request = HttpRequest()
    response = profile(request)
    html = response.content.decode('utf8')
    self.assertIn('<html>', html)
