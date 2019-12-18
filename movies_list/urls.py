from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from user.views import UserViewSet
from library.views import LibraryViewSet
from category.views import CategoryViewSet
from movie.views import MovieViewSet

router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'library', LibraryViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'movie', MovieViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('login.urls')),
    path('create_user/', include('create_user.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('user/', include('user.urls')),
    path('libraries/', include('library.urls')),
    path('categories/', include('category.urls')),
    path('movies/', include('movie.urls')),
    path('api-auth-rout/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-auth/', include(router.urls)),
]
