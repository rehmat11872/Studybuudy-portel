from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('room/<str:pk>/', views.room, name='room'),
    path('create_room/', views.CreateRoom, name='create_room'),
    path('update_room/<str:pk>/', views.UpdateRoom, name='update_room'),
    path('delete_room/<str:pk>/', views.deleteRoom, name='delete_room'),




]