from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_page(request):
   data = {}
   request.count=0
   data["new_item_text"] = request.POST.get("item_text","")
   return render(request, "lists/home.html", data)

