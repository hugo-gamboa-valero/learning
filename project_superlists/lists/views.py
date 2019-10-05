from django.shortcuts import render

# Create your views here.
def home_page(requests):
   return render(requests, template_name="lists/homepage.html")
