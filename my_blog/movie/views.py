from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from movie.models import Movie
from movie.forms import MovieForm


class MovieListView(ListView):
    model = Movie
    paginate_by = 3


class MovieDetailView(DetailView):
    model = Movie
    template_name = "movie/movie_detail.html"
    fields = ["name", "code", "description"]

    def get(self, request, pk):
        movie = Movie.objects.get(id=pk)
        comments = Comment.objects.filter(movie=movie).order_by("-updated_at")
        comment_form = CommentForm()
        context = {
            "movie": movie,
            "comments": comments,
            "comment_form": comment_form,
        }
        return render(request, self.template_name, context)


class MovieCreateView(LoginRequiredMixin, CreateView):
    model = Movie
    success_url = reverse_lazy("movie:movie-list")

    form_class = MovieForm
    # fields = ["name", "code", "description"]

    def form_valid(self, form):
        """Filter to avoid duplicate movies"""
        data = form.cleaned_data
        form.instance.owner = self.request.user
        actual_objects = Movie.objects.filter(
            name=data["name"], code=data["code"]
        ).count()
        if actual_objects:
            messages.error(
                self.request,
                f"El curso {data['name']} - {data['code']} ya está creado",
            )
            form.add_error("name", ValidationError("Acción no válida"))
            return super().form_invalid(form)
        else:
            messages.success(
                self.request,
                f"Curso {data['name']} - {data['code']} creado exitosamente!",
            )
            return super().form_valid(form)


class MovieUpdateView(LoginRequiredMixin, UpdateView):
    model = Movie
    fields = ["name", "code", "description"]

    def get_success_url(self):
        movie_id = self.kwargs["pk"]
        return reverse_lazy("movie:movie-detail", kwargs={"pk": movie_id})


class MovieDeleteView(LoginRequiredMixin, DeleteView):
    model = Movie
    success_url = reverse_lazy("movie:movie-list")


class CommentCreateView(LoginRequiredMixin, CreateView):
    def post(self, request, pk):
        movie = get_object_or_404(Movie, id=pk)
        comment = Comment(
            text=request.POST["comment_text"], owner=request.user, movie=movie
        )
        comment.save()
        return redirect(reverse("movie:movie-detail", kwargs={"pk": pk}))


class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment

    def get_success_url(self):
        movie = self.object.movie
        return reverse("movie:movie-detail", kwargs={"pk": movie.id})






def movies(request):
    movies = Movie.objects.all() 

    context_dict = {"movies": movies}

    return render(
        request=request,
        context={"movie_list": get_movies(request)},
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


def movie_detail(request, pk: int):
    return render(
        request=request,
        context={"movie": Movie.objects.get(pk=pk)},
        template_name="movie/movie_detail.html",
    )


def movie_update(request, pk: int):
    movie = Movie.objects.get(pk=pk)

    if request.method == "POST":
        movie_form = MovieForm(request.POST)
        if movie_form.is_valid():
            data = movie_form.cleaned_data
            movie.name = data["name"]
            movie.release_date = data["release_date"]
            movie.produced_by = data["produced_by"]
            movie.description = data["description"]           
            movie.save()

            return render(
                request=request,
                context={"movie": movie},
                template_name="movie/movie_detail.html",
            )

    movie_form = MovieForm(model_to_dict(movie))
    context_dict = {
        "movie": movie,
        "form": movie_form,
    }
    return render(
        request=request, context=context_dict, template_name="movie/movie_form.html"
    )

def movie_delete(request, pk: int):
    movie = Movie.objects.get(pk=pk)
    if request.method == "POST":
        movie.delete()

        movies = Movie.objects.all()
        context_dict = {"movie_list": movies}
        return render(
            request=request,
            context=context_dict,
            template_name="movie/movie_list.html",
        )

    context_dict = {
        "movie": movie,
    }
    return render(
        request=request,
        context=context_dict,
        template_name="movie/movie_delete.html",
    )



from django.core.exceptions import ValidationError
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from movie.models import Movie

class MovieListView(ListView):
    model: Movie
    paginate_by = 3


class MovieDetailView(DetailView):
    model = Movie
    template_name = "movie/movie_detail.html"
    fields = ["name", "release_date", "produced_by", "description",]

class MovieCreateView(CreateView):
    model = Movie
    success_url = reverse_lazy("movie:movie-list")

    form_class = MovieForm
    # fields = ["name", "release_date", "produced_by", "description"]

    def form_valid(self, form):
        """Filter to avoid duplicate movies"""
        data = form.cleaned_data
        actual_objects = Movie.objects.filter(
            name=data["name"], reselase_date=data["reselase_date"], produced_by=data["produced_by"],
        ).count()
        if actual_objects:
            messages.error(
                self.request,
                f"La pelicula {data['name']} - {data['reselase_date']} - {data['produced_by']} ya está creado",
            )
            form.add_error("name", ValidationError("Acción no válida"))
            return super().form_invalid(form)
        else:
            messages.success(
                self.request,
                f"movie {data['name']} - {data['reselase_date']} - {data['produced_by']} creado exitosamente!",
            )
            return super().form_valid(form)


class MovieUpdateView(UpdateView):
    model = Movie
    fields = ["name", "reselase_date", "produced_by", "description"]

    def get_success_url(self):
        movie_id = self.kwargs["pk"]
        return reverse_lazy("movie:movie-detail", kwargs={"pk": movie_id})


class MovieDeleteView(DeleteView):
    model = Movie
    success_url = reverse_lazy("movie:movie-list")
