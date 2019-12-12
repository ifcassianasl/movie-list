from django.urls import path
from . import views

urlpatterns = [
    path('', views.libraries_view, name='libraries'),
    path('create_library', views.create_library, name="create_library"),
]
