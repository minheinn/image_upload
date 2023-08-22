from django.urls import path
from . import views

urlpatterns = [
    path('', views.ShowPhoto, name="show_photo"),
    path('add-photo/', views.AddPhoto, name="add_photo"),
    path('view-photo/<str:slug>/', views.ViewPhoto, name="view_photo"),
]
