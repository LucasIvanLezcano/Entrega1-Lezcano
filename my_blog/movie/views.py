from django.shortcuts import render
from django.core.paginator import Paginator
from django.contrib import messages


from movie.models import Movie
from movie.forms import MovieForm
def movies(request):
    movies = Movie.objects.all() 

    context_dict = {"movies": movies}

    return render(
        request=request,
        context=context_dict,
        template_name="movie/movie_list.html",
    )
def get_movies(request):
    movies = Movie.objects.all()
    paginator = Paginator(movies, 3)
    page_number = request.GET.get("page")
    return paginator.get_page(page_number)


def create_movies (request):
    if request.method == "POST":
            movie_form = MovieForm(request.POST)
            if movie_form.is_valid():
                data = movie_form.cleaned_data
                actual_objects = Movie.objects.filter(
                    name=data["name"], release_date=data["release_date"], produced_by=data["produced_by"]
                ).count()
                print("actual_objects", actual_objects)
                if not actual_objects:
                    movie = Movie(
                        name=data["name"],
                        release_date=data["release_date"],
                        produced_by=data["produced_by"],
                    )
                    movie.save()
                    messages.success(
                        request,
                        f"Movie {data['name']} - {data['release_date']} - {data['produced_by']} creado exitosamente!",
                    )
                    return render(
                        request=request,
                        context={"movie_list": get_movies(request)},
                        template_name="movie/movie_list.html",
                    )
                else:
                    messages.error(
                        request,
                        f"El movie {data['name']} - {data['release_date']} - {data['produced_by']} ya está creado",
                    )



    movie_form = MovieForm(request.POST)
    context_dict = {"form": movie_form}
    return render(
        request=request,
        context=context_dict,
        template_name="movie/movie_form.html",
    )
        