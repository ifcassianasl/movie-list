from django.urls import path
from . import views

urlpatterns = [
    path('', views.movies_view, name='movies'),
    path('create_movie/', views.create_movie, name="create_movie"),
    path('delete_movie/', views.delete_movie, name="delete_movie"),
]
