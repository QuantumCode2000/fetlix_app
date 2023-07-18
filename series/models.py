"""
Aqui definimos los modelos que iran en nuestra base de datos
"""
from django.db import models
from django.db.models import CASCADE

# Create your models here.
class Serie(models.Model):
    """
    Model de Serie para la tabla en la base de datos
    """

    title = models.CharField(max_length=50)
    description = models.TextField()
    
    def __str__(self) :
        return str(self.title)

class Episode(models.Model):
    """
    Modelo de la tabla episode
    """

    number = models.IntegerField()
    name = models.CharField(max_length=50)
    serie = models.ForeignKey(Serie, on_delete=CASCADE)
    
    def __str__(self):
        return f'{self.name} - {self.number}'
    