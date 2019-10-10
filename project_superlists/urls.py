from django.conf.urls import url, include

from project_superlists.lists import views as lists_views
from project_superlists.lists import urls as list_urls

urlpatterns = [
    url(r"^$", lists_views.home_page, name="home"),
    url(r"^lists/", include(list_urls)),  
]
