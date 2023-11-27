from django.db import models

# Create your models here.
class Account(models.Model):
    username = models.CharField(max_length = 25)
    email = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)
    
    def __str__(self):
        return f"{self.username}"