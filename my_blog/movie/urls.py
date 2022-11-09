from django.urls import path

from movie import views

app_name = "movie"
urlpatterns = [
    path("movies", views.movies, name="movie-list"),
    path("movie/add", view=views.create_movies, name="movie-add"),
    path('movie/<int:pk>/detail/', views.movie_detail, name='movie-detail'),
    path('movie/<int:pk>/update/', views.movie_update, name='movie-update'),
    path('movie/<int:pk>/delete/', views.movie_delete, name='movie-delete'),





]