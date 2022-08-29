from django.test import TestCase, Client
from bs4 import BeautifulSoup
from .models import ToDo
from django.contrib.auth.models import User

class TestView(TestCase):
  def setUp(self):
    self.client = Client()
    self.user_test1 = User.objects.create_user(username='test1', password='somepassword')
    self.user_test2 = User.objects.create_user(username='test2', password='somepassword')