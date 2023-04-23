from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class UserUniModel(AbstractUser):
    phone = models.CharField(max_length=13)
    image = models.ImageField()