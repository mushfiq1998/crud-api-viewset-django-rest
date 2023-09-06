from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer

class StudentViewset(viewsets.ViewSet):

    def list(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        id = pk
        if id is not None:
            student = Student.objects.get(id=id)
            serializer = StudentSerializer(student)
            return Response(serializer.data)
    
    def create(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data created'}, 
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, 
                            status=status.HTTP_400_BAD_REQUEST)
    
    
    def update(self, request, pk):
        id = pk
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Complete data Updated'})
        return Response(serializer.errors, 
                            status=status.HTTP_400_BAD_REQUEST)
    
    
    def partial_update(self, request, pk):
        id = pk
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student, data=request.data,
                                       partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partial data Updated'})
        return Response(serializer.errors, 
                            status=status.HTTP_400_BAD_REQUEST)
    
    
    def destroy(self, request, pk):
        id = pk
        student = Student.objects.get(id=id)
        student.delete()
        return Response({'msg': 'Data deleted'})
