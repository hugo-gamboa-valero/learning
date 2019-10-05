from django.conf.urls import url, include

from project_superlists.lists import views as lists_views

urlpatterns = [
    url(r'', lists_views.home_page),
]
