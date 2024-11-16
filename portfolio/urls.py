# Import the path function for URL configuration
from django.urls import path
from . import views

# Define the app name for namespacing URLs in templates and other places
app_name = 'portfolio'

# URL patterns for the portfolio app
urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('thank_you/', views.thank_you, name='thank_you'),
]
