from django.urls import path
from . import views

urlpatterns = [
    path('', views.ShowPhoto, name="show_photo"),
    path('add-photo/', views.AddPhoto, name="add_photo"),
    path('view-photo/<str:pk>/', views.ViewPhoto, name="view_photo"),
]
