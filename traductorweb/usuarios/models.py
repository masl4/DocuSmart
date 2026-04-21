from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):  # modelo de usuario de Django
    email = models.EmailField(unique=True)  # Email único y obligatorio
    bio = models.TextField(blank=True, null=True)  # Campo opcional de biografía

    def __str__(self):
        return self.username
