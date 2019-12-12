from django.urls import path
from . import views

urlpatterns = [
    path('', views.account, name="account"),
    path('edit_account/', views.edit_account, name="edit_account"),
]
