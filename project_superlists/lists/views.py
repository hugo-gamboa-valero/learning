from django.shortcuts import render

# Create your views here.
def homepage(requests):
   return render(requests, template_name="lists/homepage.html")
