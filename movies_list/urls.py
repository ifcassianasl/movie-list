from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('login.urls')),
    path('create_user/', include('create_user.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('user/', include('user.urls')),
    path('libraries/', include('library.urls')),
    path('categories/', include('category.urls')),
    path('movies/', include('movie.urls')),
]
