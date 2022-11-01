from django.shortcuts import render
from django.core.paginator import Paginator
from django.contrib import messages


from actor.models import Actor
from actor.forms import ActorForm  

def actors(request):
    actors = Actor.objects.all() 

    context_dict = {"actors": actors}

    return render(
        request=request,
        context=context_dict,
        template_name="actor/actor_list.html",
    )
def get_actors(request):
    actors = Actor.objects.all()
    paginator = Paginator(actors, 3)
    page_number = request.GET.get("page")
    return paginator.get_page(page_number)



def create_actors(request):
    if request.method == "POST":
        actor_form = ActorForm(request.POST)
        if actor_form.is_valid():
            data = actor_form.cleaned_data
            actual_objects = Actor.objects.filter(
                name=data["name"], last_name=data["last_name"], awards=data["awards"]
            ).count()
            print("actual_objects", actual_objects)
            if not actual_objects:
                actor = Actor(
                    name=data["name"],
                    last_name=data["last_name"],
                    awards=data["awards"],
                )
                actor.save()
                messages.success(
                    request,
                    f"Actor {data['name']} - {data['last_name']} - {data['awards']} creado exitosamente!",
                )
                return render(
                    request=request,
                    context={"actor_list": get_actors(request)},
                    template_name="actor/actor_list.html",
                )
            else:
                messages.error(
                    request,
                    f"El actor {data['name']} - {data['last_name']} - {data['awards']} ya está creado",
                )



    actor_form = ActorForm(request.POST)
    context_dict = {"form": actor_form}
    return render(
        request=request,
        context=context_dict,
        template_name="actor/actor_form.html",
    )




            

    