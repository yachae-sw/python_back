from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser

class User(AbstractUser):
    nickname = models.CharField(max_length=30)
    
    class Meta:
        db_table="user"

