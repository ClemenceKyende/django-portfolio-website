from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Contact  # Import the Contact model to save form data into the database

# View for rendering the homepage of the portfolio
def index(request):
    return render(request, 'portfolio/index.html') # Renders the 'index.html' template

# View for handling the contact form submission
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Manually create and save the Contact object
            Contact.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['phone'],
                message=form.cleaned_data['message']
            )
            return redirect('portfolio:thank_you')  # Redirect after successful form submission
    else:
        form = ContactForm()

    return render(request, 'portfolio/contact.html', {'form': form})

# Redirect the user to a 'thank you' page after successful submission
def thank_you(request):
    return render(request, 'portfolio/thank_you.html')
