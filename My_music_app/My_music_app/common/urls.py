from django.urls import path

from My_music_app.common import views


urlpatterns = [
    path('', views.home_page, name='home page')
]