from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

from .views import home_page

# Create your tests here.
class HomePageTest(TestCase):
   def test_home_page_returns_correct_html(self):
      response = self.client.get("/") 
      self.assertTemplateUsed(response, "lists/home.html") 

#   def test_input_keys(self):
#      request = HttpRequest()
#      response = home_page(request)
#      html = response.content.decode("utf8")
#      self.
      
