from django.db import models

# Create your models here.
class Corpo(models.Model):
    tgc                 = models.FloatField()
    musculo             = models.FloatField()
    umidade             = models.FloatField()
    massa_ossea         = models.FloatField()
    tmb                 = models.FloatField()
    taxa_proteica       = models.FloatField()
    idade_corporal      = models.IntegerField()
    gordura_viceral     = models.IntegerField()
    gordura_subcutanea  = models.FloatField()
    peso_ideal          = models.FloatField()
    gordura_corporal    = models.FloatField()
    peso_sem_gordura    = models.FloatField()
    peso_muscular       = models.FloatField()
    quantidade_proteina = models.FloatField()