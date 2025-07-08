from django.db import models

# Create your models here.
class Singer(models.Model):
  id = models.AutoField(primary_key=True)
  content = models.TextField() # 가수설명
  debut = models.DateField() # 데뷔일자
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)


class Song(models.Model):
  singer = models.ForeignKey(Singer, on_delete=models.CASCADE, related_name='songs')
  title = models.CharField(max_length=100)
  release_date = models.DateField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)