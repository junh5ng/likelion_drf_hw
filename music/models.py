from django.db import models

# Create your models here.
class Singer(models.Model):
  content = models.TextField() # 가수설명
  debut = models.DateField() # 데뷔일자

  def __str__(self):
    return self.content[:30]
  

class Song(models.Model):
  singer = models.ForeignKey(Singer, on_delete=models.CASCADE, related_name="songs")
  release = models.DateField() # 출시일자
  content = models.TextField() # 노래설명

  def __str__(self):
    return self.content[:30]