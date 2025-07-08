from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Singer, Song
from .serializers import SingerSerializer, SongSerializer

@api_view(['GET', 'POSt'])
def singer_list(request):
  if request.method == 'GET':
    singers = Singer.objects.all()
    serializer = SingerSerializer(singers, many=True)
    return Response(serializer.data)
  elif request.method == 'POST':
    serializer = SingerSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
  
@api_view(['GET', 'POSt'])
def song_list(request):
  if request.method == 'GET':
    songs = Song.objects.all()
    serializer = SongSerializer(songs, many=True)
    return Response(serializer.data)
  elif request.method == 'POST':
    serializer = SongSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)