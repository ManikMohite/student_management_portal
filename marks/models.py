from django.db import models
from students.models import Student

class Mark(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    internal = models.IntegerField()
    external = models.IntegerField()

    @property
    def total(self):
        return self.internal + self.external

    def __str__(self):
        return f"{self.student.user.username} - {self.subject}"