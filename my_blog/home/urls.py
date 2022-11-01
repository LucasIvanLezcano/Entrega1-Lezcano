from django.urls import path

from home import views

app_name = "home"
urlpatterns = [
    path("", views.index, name="home"),
    path("search/", views.search, name="search"),
]