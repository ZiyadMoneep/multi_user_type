from datetime import timezone
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class User(AbstractUser):
    is_Recruiter = models.BooleanField(default=False)
    is_Applicant = models.BooleanField(default=False)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    username = models.CharField(max_length=250, unique=True)
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField(null=True, blank=True)


class Recruiter(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    phone_number = models.PositiveIntegerField(null=True, blank=True)
    company_name = models.CharField(max_length=150, null=True, blank=True)
    company_description = models.CharField(max_length=300, null=True, blank=True)
    website = models.CharField(max_length=100, default="")

    def __str__(self):
        return f"{self.user.username} {self.company_name} "


class Applicant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    phone_number = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} {self.user.age} "
