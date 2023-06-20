from django.urls import path

from My_music_app.user_profile import views

urlpatterns = [
    path('details/', views.profile_details, name='profile details'),
    path('delete/', views.profile_delete, name='profile delete'),
]

