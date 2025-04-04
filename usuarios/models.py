from django.core.validators import MaxValueValidator , MinValueValidator
from django.contrib.auth.models import AbstractUser
from django.db import models

class UserAbs(AbstractUser):
    fone = models.CharField(max_length=15)


    def __str__(self):
        return self.fone