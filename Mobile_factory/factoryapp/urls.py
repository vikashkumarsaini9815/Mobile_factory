from django.contrib import admin
from django.urls import path, include
from factoryapp import views
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mobile/',MobileAPIView.as_view(),name='MobileAPIView')
]