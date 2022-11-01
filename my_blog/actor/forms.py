#from ckeditor.widgets import CKEditorWidget
from django import forms


from actor.models import Actor

class ActorForm(forms.Form):
    name = forms.CharField(
        label="Nombre del actor/actriz",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "actor-name",
                "placeholder": "introduzca nombre",
                "required": "True",
            }
        ),
    )
    last_name = forms.CharField(
        label="Apellido del actor/actriz",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "actor-last_name",
                "placeholder": "introduzca apellido",
                "required": "True",
            }
        ),
    )
    awards = forms.IntegerField(
        label="Premios del actor/a",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "actor-awards",
                "placeholder": "introduzca cantidad de premios",
                "required": "True",
            }
        ),
    )

    class Meta:
        model = Actor
        fields = ["name", "last_name", "awards"]