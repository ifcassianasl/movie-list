from django.urls import path
from . import views

urlpatterns = [
    path('', views.libraries_view, name='libraries'),
    path('create_library/', views.create_library, name="create_library"),
    path('delete_library/', views.delete_library, name="delete_library"),
    path('active_library/', views.active_library, name="active_library"),
]
