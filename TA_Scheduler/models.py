from django.db import models

# Create your models here.
class UserType(models.TextChoices):
    Supervisor = "S"
    Instructor = "I"
    TA = "T"

class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    accountType = models.CharField(max_length=1, choices=UserType.choices, default=UserType.TA)

class Course(models.Model):
    name = models.CharField(max_length=20)
    number = models.IntegerField()

class CourseAssignment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    