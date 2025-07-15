from rest_framework import serializers
from .models import *

class SingerImageSerializer(serializers.ModelSerializer):
  class Meta:
    model = SingerImage
    fields = '__all__'

class SingerSerializer(serializers.ModelSerializer):
  id = serializers.CharField(read_only=True)
  created_at = serializers.CharField(read_only=True)
  updated_at = serializers.CharField(read_only=True)

  # 댓글처럼 Song 목록을 추가
  songs = serializers.SerializerMethodField(read_only=True)

  def get_songs(self, instance):
      serializer = SongSerializer(instance.songs.all(), many=True)
      return serializer.data
  
  tags = serializers.SerializerMethodField()

  def get_tags(self, instance):
    tag = instance.tags.all()
    return [t.name for t in tag]
  
  class Meta:
    model = Singer
    fields = '__all__'

  image = SingerImageSerializer(many=True, read_only = True)
  #image = serializers.ImageField(use_url=True, required=False)


class SongSerializer(serializers.ModelSerializer):
  class Meta:
      model = Song
      fields = '__all__'
      read_only_fields = ['singer']


class TagSerializer(serializers.ModelSerializer):
    
    class Meta:
      model = Tag
      fields = '__all__'