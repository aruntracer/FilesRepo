from django.db import models

# Create your models here.
class users(models.Model):
    first_name = models.CharField(max_length=256,unique=True)
    last_name = models.CharField(max_length=256, unique=True)
    Email = models.EmailField(max_length=256,unique=True)

    def __str__(self):
        return self.first_name+", "+self.last_name+", "+self.Email
