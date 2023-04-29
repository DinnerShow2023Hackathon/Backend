from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from dinner.models import User, Bookpost
from rest_framework import status
from rest_framework.response import Response
from dinner.serializers import UserSerializer, BookpostSerializer
# Create your views here.

def index(request):
    return HttpResponse('It\'s dinnershow')

def findID(nickname):
    user = User.objects.get(nickname=nickname)
    id = user.id
    return id

@api_view(['POST'])
def signup(request, nickname):
    if request.method == 'POST':
        data = request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def addBook(request, nickname):
    if request.method == 'POST':
        data = request.data
        serializer = BookpostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def getMyBooks(request, nickname):
    if request.method == 'GET':
        id = findID(nickname)
        books = Bookpost.objects.filter(whos=id)
        serializer = BookpostSerializer(books, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def getAllBooks(request):
    if request.method == 'GET':
        books = Bookpost.objects.all()
        serializer = BookpostSerializer(books, many=True)
        return Response(serializer.data)