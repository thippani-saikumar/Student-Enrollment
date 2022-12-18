from django.db import models

# Create your models here.
class user(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=80)
