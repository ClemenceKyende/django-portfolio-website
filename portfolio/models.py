# Import Django's ORM models
from django.db import models

# Define a model for storing contact form submissions
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    message = models.TextField()

    # Define the string representation of the model, which will display the contact's name
    def __str__(self):
        return self.name
