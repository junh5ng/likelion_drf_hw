from django.urls import path
from . import views
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.singer_list_create),
    path('<int:singer_id>', views.singer_detail_update_delete),
    path('<int:singer_id>/songs', views.song_read_create),
    path('tags/<str:tags_name>', views.find_tag),
    path('<int:singer_id>/image', views.singer_image_create),
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
