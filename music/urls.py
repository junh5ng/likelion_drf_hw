from django.urls import path
from . import views

urlpatterns = [
    path('singers/', views.singer_list),
    path('songs/', views.song_list),
]
