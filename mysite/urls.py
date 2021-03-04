from django.contrib import admin
from django.urls import path, include
import shop

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls')),
]
