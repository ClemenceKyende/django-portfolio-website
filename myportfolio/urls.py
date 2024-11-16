from django.contrib import admin
from django.urls import path, include

#porfolio app URLs
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portfolio.urls')),
]
