from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Device(models.Model):
    name = models.CharField(max_length=255, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)


    def __str__(self):
        return self.name
