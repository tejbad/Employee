from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import auth
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

# class UserProfile(models.Model):
    
class User(AbstractUser):
    # emp_type = models.CharField(max_length=20, default="")
    total_leaves_left = models.IntegerField(default=00,blank=False)


