from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_view, name="create_user"),
]
