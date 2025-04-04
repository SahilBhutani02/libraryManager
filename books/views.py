from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from .models import BooksModel
from .serializers import BooksSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination

class BooksView(APIView):
    def get(self, request):
        books = BooksModel.objects.all()

        # Manually apply pagination
        paginator = PageNumberPagination()  
        paginated_queryset = paginator.paginate_queryset(books, request)
        serializer = BooksSerializer(paginated_queryset, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = BooksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BooksIDView(APIView):
    def get(self, request, pk):
        book = get_object_or_404(BooksModel, pk=pk)
        serializer = BooksSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        book = get_object_or_404(BooksModel, pk=pk)
        serializer = BooksSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        book = get_object_or_404(BooksModel, pk=pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
