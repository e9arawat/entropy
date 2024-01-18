from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Manager(AbstractUser):
    is_admin = models.BooleanField(default=True)