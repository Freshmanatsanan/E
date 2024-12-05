from django.db import models

# Create your models here.

class Course(models.Model):
    course_id = models.CharField(max_length=50, unique=True)
    course_name = models.CharField(max_length=200)