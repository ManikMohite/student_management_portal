from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roll_no = models.CharField(max_length=20)
    department = models.CharField(max_length=100)
    semester = models.IntegerField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    photo = models.ImageField(upload_to='students/', blank=True, null=True)

    def __str__(self):
        return self.user.username