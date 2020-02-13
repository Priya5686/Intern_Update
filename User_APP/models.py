from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    descripition = models.CharField(max_length=50, default="")
    city = models.CharField(max_length=50, default="")
    phone = models.IntegerField(default=0)
    website = models.URLField(default="")


