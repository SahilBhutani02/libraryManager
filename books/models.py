from django.db import models
from students.models import StudentsModel

class BooksModel(models.Model):
    book_id = models.CharField(max_length=10, unique=True)
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    publication = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    issued_to = models.ForeignKey(StudentsModel, on_delete=models.SET_NULL, null=True, blank=True,  related_name="books")

    # issued_to = models.ForeignKey(
    #     StudentsModel,
    #     on_delete=models.SET_NULL,
    #     null=True,
    #     blank=True,
    #     to_field="student_id"  # Link to student_id instead of id
    # ) 

    def __str__(self):
        return self.title
