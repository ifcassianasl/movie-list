from django.urls import path
from . import views

urlpatterns = [
    path('', views.categories_view, name='categories'),
    path('create_category/', views.create_categories, name="create_category"),
    path('delete_category/', views.delete_category, name="delete_category"),
]
