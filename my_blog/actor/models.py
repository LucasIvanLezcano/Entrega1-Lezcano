from django.db import models

class Actor(models.Model):
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    awards = models.IntegerField()

    def __str__(self):
        return f"Name:{self.name} - Last_name: {self.last_name} - Awards: {self.awards}"