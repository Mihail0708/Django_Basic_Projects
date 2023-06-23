from django.urls import path, include

from Car_collection_app.web import views

urlpatterns = [
    path('', views.home_page, name='home page'),
    path('catalogue/', views.catalogue, name='catalogue'),
    path('profile/', include([
        path('create/', views.profile_create, name='profile create'),
        path('delete/', views.profile_delete, name='profile delete'),
        path('edit/', views.profile_edit, name='profile edit'),
        path('details/', views.profile_details, name='profile details'),
    ])),
    path('car/create/', views.car_create, name='car create'),
    path('car/<int:pk>/', include([
        path('details/', views.car_details, name='car details'),
        path('edit/', views.car_edit, name='car edit'),
        path('delete/', views.car_delete, name='car delete'),
    ]))
]
