from django.db import models

class StudentsModel(models.Model):
    student_id = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=50)
    stream = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    address = models.TextField()

    def __str__(self):
        return self.name
