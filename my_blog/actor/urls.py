from django.urls import path

from actor import views

app_name = "actor"
urlpatterns = [
    path("actors", views.actors, name="actor-list"),
    path("actor/add", view=views.create_actors, name="actor-add"),
]