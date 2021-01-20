from django.db import models

# Create your models here.
class testU(models.Model) :
    GENDERS = (('M','남성(M)'),('W','여성(W)'))
    username = models.CharField(max_length=64, verbose_name='이름')
    gender = models.CharField(max_length=1, verbose_name='성별', choices=GENDERS)
    birthday = models.DateField(null=True, blank=True)
