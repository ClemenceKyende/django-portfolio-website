# Django Portfolio Website

This is a personal portfolio website built with Django. It showcases my skills, projects, and professional background. The website includes a contact form where visitors can leave messages. All submissions are stored in a database for easy access and management.

## Features

- **Home Page**- Showcases a professional overview and key sections.
- **Contact Form**- Users can submit their contact details and message.
- **Responsive Design**- Fully responsive across different devices (desktop, tablet, mobile).
- **Database Integration**- Submissions from the contact form are stored in a database.

## Installation

Follow these steps to run the project locally:

### 1. Clone the Repository

Clone this repository to your local machine
git clone  https://github.com/ClemenceKyende/django-portfolio-website.git

**2. Create a Project Directory**
Navigate to the directory and set up the environment:
mkdir django_portfolio
cd django_portfolio

**Install Dependencies**
To install all necessary dependencies for this project, run the following command in your terminal or command prompt.
pip install -r requirements.txt

**3. Set Up a Virtual Environment**
Create and activate a virtual environment:

**Windows**
python -m venv venv
venv\Scripts\activate

**Mac/Linux**
python3 -m venv venv
source venv/bin/activate

**4.Install Django**
Install Django and other required packages
pip install django

**5. Create the Django Project**
Start a new Django project
django-admin startproject myportfolio .

**6. Set Up Your Django App**
Create a new app for the portfolio
python manage.py startapp portfolio

**7. Set Up the Database**
Apply migrations to set up the database
python manage.py migrate

**8. Create a Superuser (Optional)**
To access the admin panel, create a superuser
python manage.py createsuperuser
Follow the prompts to set up credentials.

**9. Run the Development Server**
Start the development server
python manage.py runserver
Visit the website at http://127.0.0.1:8000/.

**Project Structure**

django_portfolio/
├── myportfolio/                  # Main project folder
│   ├── portfolio/                # Django app
│   │   ├── migrations/           # Database migrations
│   │   ├── templates/portfolio/  # HTML templates
│   │   ├── static/portfolio/     # CSS and static assets
│   │   ├── forms.py              # Contact form definitions
│   │   ├── models.py             # Database models
│   │   ├── views.py              # Application views
│   │   ├── urls.py               # App URL routing
├── manage.py                     # Django management script
├── requirements.txt              # Dependencies for the project
├── README.md                     # Project documentation 


**Contact Form Submission**
The contact form includes the following fields.
**Name**
**Email**
**Phone**
**Message**
Each submission is validated and stored in the database. Upon submission, users are redirected to a "Thank You" page.

**Technologies Used**
**Django** - High-level Python web framework.
**Bootstrap** - CSS framework for responsive design.
**SQLite** - Development database (replaceable with other options like PostgreSQL).

**License**
This project is licensed under the MIT License. See the LICENSE file for more details.