from django import forms
from ckeditor.widgets import CKEditorWidget

from movie.models import Movie

class MovieForm(forms.ModelForm):
    name = forms.CharField(
        label="Nombre de la pelicula",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "movie-name",
                "placeholder": "introduzca nombre de la pelicula",
                "required": "True",
            }
        ),
    )
    
    release_date = forms.DateField(
        label="NFecha de estreno",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "movie-name",
                "placeholder": "introduzca fecha de estreno",
                "required": "True",
            }
        ),
    )
    produced_by = forms.CharField(
        label="Dirigida por : ",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "movie-produced_by",
                "placeholder": "introduzca nombre del director/a",
                "required": "True",
            }
        ),
    )

    description = forms.CharField(
        label="Descripción:",
        required=False,
        widget=CKEditorWidget(
            attrs={
                "class": "movie-description",
                "placeholder": "Descripcion de la pelicula",
                "required": "True",
            }
        ),
    )
    class Meta:
        model = Movie
        fields = ["name", "release_date", "produced_by", "description"] 