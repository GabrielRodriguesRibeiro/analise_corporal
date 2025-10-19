from django.db import models

# Create your models here.
class Usuario(models.Model):
    email = models.EmailField(blank=False, max_length=60)
    senha = models.CharField(blank=False, max_length=60)