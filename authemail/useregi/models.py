from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email_verified = models.BooleanField(default=False)
    verification_token = models.CharField(max_length=40, blank=True, null=True)