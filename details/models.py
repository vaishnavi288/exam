from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=20)
    roll_number=models.IntegerField()
    course=models.CharField(max_length=30)
    age=models.IntegerField()
    place=models.CharField(max_length=30)
    image=models.ImageField(upload_to='media')