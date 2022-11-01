from django import forms


from director.models import Director

class DirectorForm(forms.Form):
    name = forms.CharField(
        label="Nombre del director/a",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "director-name",
                "placeholder": "introduzca nombre",
                "required": "True",
            }
        ),
    )   
    last_name = forms.CharField(
        label="apellido del director/a",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "director-last_name",
                "placeholder": "introduzca apellido",
                "required": "True",
            }      
        ),
    )
    birth = forms.DateField(
        label="fecha de nacimiento",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "director-birth",
                "placeholder": "introduzca fecha de nacimiento",
                "required": "True",
            }
        ),
    )
    movies = forms.IntegerField(
        label="cantidad de peliculas",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "director-movies",
                "placeholder": "introduzca cantidad de peliculas",
                "required": "True",
            }
        ),
    )
    class Meta:
        model = Director
        fields = ["name", "last_name", "birth", "movies",]


