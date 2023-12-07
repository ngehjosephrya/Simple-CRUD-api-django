from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TasksSerializer
from .models import Task 



@api_view(['GET'])
def api(request):
    api_urls = {
        'List': '/task/',
        'Detail View': '/task/<str:pk>/',
        'Create': '/create/',
        'Update': '/update/<str:pk>/',
        'Delete': '/delete/<str:pk>/',
    }
    return Response(api_urls)


@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all()
    serializer = TasksSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def taskDetail(request,pk):
    tasks = Task.objects.get(id=pk)
    serializer = TasksSerializer(tasks, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def taskCreate(request):
    serializer = TasksSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        
    return Response(serializer.data)

@api_view(['POST'])
def taskUpdate(request, pk):
    tasks = Task.objects.get(id=pk)
    serializer = TasksSerializer(instance=tasks, data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        
    return Response(serializer.data)

@api_view(['DELETE'])
def taskDelete(request, pk):
    tasks = Task.objects.get(id=pk)
    tasks.delete()
        
    return Response("Item successfully deleted!")


