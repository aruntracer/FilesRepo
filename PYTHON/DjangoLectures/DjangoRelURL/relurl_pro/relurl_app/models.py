from django.db import models

# Create your models here.
class employee(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField(default=0)
    Dept = models.CharField(max_length=30)
