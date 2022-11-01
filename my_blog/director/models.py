from django.db import models

class Director(models.Model):
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    birth = models.DateField()
    movies = models.IntegerField()

    def __str__(self):
        return f"Name: {self.name} - Last_name: {self.last_name} - Birth: {self.birth} - Movies: {self.movies}"