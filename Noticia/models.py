from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField


class Noticia(models.Model):
    titulo = models.CharField(max_length=255)
    titulo_cartel = models.CharField(max_length=255)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    cuerpo = RichTextField(blank=True, null=True)
    fecha_noticia = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo + ' | ' + str(self.autor)

    def get_absolute_url(self):
        return reverse('home')

        
