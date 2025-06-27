from django.db import models
# from django.utils import timezone

class Member(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.IntegerField(null = True)
    joined_date = models.DateField(null = True) #
# Create your models here.
