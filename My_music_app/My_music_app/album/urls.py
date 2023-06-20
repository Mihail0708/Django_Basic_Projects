from django.urls import path

from My_music_app.album import views

urlpatterns = [
    path('add/', views.album_add, name='add album'),
    path('details/<int:pk>/', views.album_details, name='details album'),
    path('edit/<int:pk>/', views.album_edit, name='edit album'),
    path('delete/<int:pk>/', views.album_delete, name='delete album')
]