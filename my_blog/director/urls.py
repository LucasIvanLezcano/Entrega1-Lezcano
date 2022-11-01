from django.urls import path

from director import views

app_name = "director"
urlpatterns = [
    path("directors", views.directors, name="director-list"),
    path("director/add", view=views.create_directors, name="director-add"),
]