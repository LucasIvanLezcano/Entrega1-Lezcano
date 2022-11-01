from django.shortcuts import render
from django.core.paginator import Paginator
from django.contrib import messages


from director.models import Director
from director.forms import DirectorForm

def directors(request):
    directors = Director.objects.all() 

    context_dict = {"directors": directors}

    return render(
        request=request,
        context=context_dict,
        template_name="director/director_list.html",
        ) 
def get_directors(request):
    directors = Director.objects.all()
    paginator = Paginator(directors, 3)
    page_number = request.GET.get("page")
    return paginator.get_page(page_number)

def create_directors (request):
    if request.method == "POST":
            director_form = DirectorForm(request.POST)
            if director_form.is_valid():
                data = director_form.cleaned_data
                actual_objects = Director.objects.filter(
                    name=data["name"], last_name=data["last_name"], birth=data["birth"], movies=data["movies"]
                ).count()
                print("actual_objects", actual_objects)
                if not actual_objects:
                    director = Director(
                        name=data["name"],
                        last_name=data["last_name"],
                        birth=data["birth"],
                        movies=data["movies"],
                        
                    )
                    director.save()
                    messages.success(
                        request,
                        f"Director {data['name']} - {data['last_name']} - {data['birth']} - {data['movies']} creado exitosamente!",
                    )
                    return render(
                        request=request,
                        context={"director_list": get_directors(request)},
                        template_name="director/director_list.html",
                    )
                else:
                    messages.error(
                        request,
                        f"El director {data['name']} - {data['last_name']} - {data['birth']} - {data['movies']} ya está creado",
                    )



    director_form = DirectorForm(request.POST)
    context_dict = {"form": director_form}
    return render(
        request=request,
        context=context_dict,
        template_name="director/director_form.html",
    )
        