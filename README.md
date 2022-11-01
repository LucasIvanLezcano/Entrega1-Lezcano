Proyecto entregable para CODERHOUSE, actividad "Entrega intermedia de tu proyecto Final".
En Git bash o bash
Realizar un:
```bash
git clone https://github.com/LucasIvanLezcano/Entrega1-Lezcano.git

Ya cuenta con una base de datos para mostrar su contenido. 

Entrar en el directorio del proyecto.


```bash
cd entrega_intermedia
```
En bash tipear para entrar en el IDE de VisualStudioCode.


```bash
code .
```
en el terminal para crear el ambiente de desarrollo "venv".

```bash
python -m venv venv

venv/Scrips/activate
```

instalar los requerimientos para ejecutar el proyecto:
```bash
pip install -r requirements.txt
```

crear un super usuario para explorar la url de admin.
```bash
python manage.py createsuperuser
```

ejecutar el servidor:

```bash
python manage.py runserver
```


Para este blog se crearon 3 aplicaciones , cada una con su respectiva clase en models.py ,sus viastas en views.py , forms.py y plantillas en templates.
Cada una de las aplicaciones tiene un formulario para insertar datos a las clases de models.
Tambien cuenta con un "buscador" en la pagina principal donde se puede buscar en la base de datos de la aplicacion movie.