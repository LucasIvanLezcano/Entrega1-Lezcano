from django.shortcuts import render
from django.db.models import Q

from actor.models import Actor
from director.models import Director
from movie.models import Movie

def index(request):
    return render(
        request=request,
        context={},
        template_name="home/index.html",
    )

def search(request):
    search_param = request.GET["search_param"]
    print("search: ", search_param)
    context_dict = dict()
    if search_param:
        query = Q(name__contains=search_param)
        query.add(Q(release_date__contains=search_param), Q.OR)
        movies = Movie.objects.filter(query)
        context_dict.update(
            {
               "search_param": search_param,
                "movies": movies
               
            }
        )
    return render(
        request=request,
        context=context_dict,
        template_name="home/index.html",
    )
