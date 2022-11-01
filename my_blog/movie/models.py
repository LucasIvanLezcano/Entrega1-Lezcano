from django.db import models


class Movie(models.Model):
    name = models.CharField(max_length=40)
    release_date = models.DateField()
    produced_by = models.CharField(max_length=40)

    def __str__(self):
        return f"Name: {self.name} - Release_date: {self.release_date} - Produced_by: {self.produced_by}"
    


