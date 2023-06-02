from django.db import models
from django.contrib.auth.models import User
import os

# Create your models here.
class Anuncio(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/anuncios')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

   # def __str__(self):
    #    return self.name + '- Creado : ' +str(self.created_at)