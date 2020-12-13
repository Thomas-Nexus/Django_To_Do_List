from .views import *
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', todo, name='todo'),
    path('change/<str:pk>/', change, name='change'),
    path('remove/<str:pk>/', remove, name='remove'),
]
