from django.db import models
from django.contrib.auth.models import User

class Biblioteca(models.Model):
    nombre = models.CharField(max_length=100)
    genero = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=500)
    imagen = models.ImageField(upload_to="estanteria", null=True, blank=True)
    book = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="book")

    @property
    def image_url(self):
        return self.imagen.url if self.imagen else ""
    
    def __str__(self):
        return f"{self.id} - {self.nombre} - {self.book.id}"
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    avatar = models.ImageField(upload_to="avatares", null=True, blank=True)


    



