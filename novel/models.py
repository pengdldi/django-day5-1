from django.db import models

# Create your models here.
class Charac(models.Model) :
    name = models.CharField(max_length=64, verbose_name='이름')
