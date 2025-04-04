from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from .models import StudentsModel
from .serializers import StudentsSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination

class StudentsView(APIView):
    def get(self, request):
        students = StudentsModel.objects.all()
         # Manually apply pagination
        paginator = PageNumberPagination()  
        paginated_queryset = paginator.paginate_queryset(students, request)
        serializer = StudentsSerializer(paginated_queryset, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = StudentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentsIDView(APIView):
    def get(self, request, pk):
        student = get_object_or_404(StudentsModel, pk=pk)
        serializer = StudentsSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        student = get_object_or_404(StudentsModel, pk=pk)
        serializer = StudentsSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        student = get_object_or_404(StudentsModel, pk=pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
