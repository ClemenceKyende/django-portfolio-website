# Import Django's admin module for managing models via the admin interface
from django.contrib import admin

# Import the Contact model from the current app's models.py
from .models import Contact

# Register the Contact model with the admin interface
admin.site.register(Contact)
