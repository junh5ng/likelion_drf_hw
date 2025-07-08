from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.singer_list_create),
    path('<int:singer_id>', views.singer_detail_update_delete),
]
