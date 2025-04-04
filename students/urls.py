from django.urls import path
from . import views

urlpatterns = [
    path('students/',views.StudentsView.as_view()),
    path('students/<int:pk>',views.StudentsIDView.as_view()),
]

