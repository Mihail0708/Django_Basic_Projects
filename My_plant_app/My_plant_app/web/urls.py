from django.urls import path, include

from My_plant_app.web import views

urlpatterns = [
    path('', views.home_page, name='home page'),
    path('catalogue/', views.catalogue, name='catalogue'),
    path('create/', views.plant_create, name='plant create'),
    path('details/<int:pk>/', views.plant_details, name='plant details'),
    path('edit/<int:pk>/', views.plant_edit, name='plant edit'),
    path('delete/<int:pk>/', views.plant_delete, name='plant delete'),
    path('profile/', include([
        path('create/', views.profile_create, name='profile create'),
        path('details/', views.profile_details, name='profile details'),
        path('edit/', views.profile_edit, name='profile edit'),
        path('delete/', views.profile_delete, name='profile delete'),
    ]))
]


