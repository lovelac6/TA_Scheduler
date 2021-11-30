from django.db import models

# Create your models here.
class UserType(models.TextChoices):
    Supervisor = "S"
    Instructor = "I"
    TA = "T"

class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

class AccountType(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    accountType = models.CharField(max_length=1, choices=UserType.choices, default="T")

