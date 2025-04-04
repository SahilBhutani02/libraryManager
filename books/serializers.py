from rest_framework import serializers
from .models import BooksModel
from students.serializers import StudentsSerializer
from students.models import StudentsModel

class BooksSerializer(serializers.ModelSerializer):
    # issued_to = StudentsSerializer(read_only=True)  # Show student details in book response

    issued_to = serializers.SlugRelatedField(
        queryset=StudentsModel.objects.all(),
        slug_field='student_id',  # Accepts student_id for issuing
        allow_null=True,
        # write_only=True  # Accepts input but won't show in response
    )
    
    student_details = StudentsSerializer(source="issued_to", read_only=True)  # Show full student details

    class Meta:
        model = BooksModel
        fields = ['id', 'book_id', 'title', 'author', 'publication', 'price', 'issued_to', 'student_details']