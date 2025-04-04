from rest_framework import serializers
from .models import StudentsModel
# from books.serializers import BooksSerializer


class StudentsSerializer(serializers.ModelSerializer):
    # books_issued = BooksSerializer(many=True, read_only=True)  # Show books issued to a student

    class Meta:
        model = StudentsModel
        fields = '__all__'