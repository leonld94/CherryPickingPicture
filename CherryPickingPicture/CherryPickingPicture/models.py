from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Picture(models.Model):
    uploader = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="")