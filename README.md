Sustainify 🌱 - Eco-conscious E-Commerce Platform
Developer: Idah Lindiwe Khumalo
Location: City of Johannesburg, Gauteng, South Africa
Contact: +27671114441 / +27780542966 / +27768338122
Email: lindiwekhumalo833@gmail.com
LinkedIn: https://www.linkedin.com/in/idah-khumalo-765778159
GitHub: https://github.com/Shantralee-58

Project Description
Sustainify is an eco-conscious full-stack e-commerce and service platform built with Django. The platform connects users with verified sustainable products, provides a robust API for order management, and promotes ethical consumption. Sustainify emphasizes sustainability, user empowerment, and ethical consumption by allowing users to:

Browse products via categories and search.

Securely place and track orders.

View contact and store location information.

💻 Tech Stack
Component

Technology

Notes

Backend Framework

Django 5.x (Python 3.12)

Provides ORM, routing, and security.

API

Django REST Framework (DRF)

Used for secure, authenticated order placement and product listing.

Database

SQLite (Development)

Lightweight and default database for local testing.

Frontend

HTML, CSS (Custom), JavaScript

Focus on clean, responsive UI.

Authentication

Django's built-in Auth system

Handles user registration, login, and password management.

🚀 Setup Instructions
Follow these steps to set up and run the project locally.

1. Prerequisites
Ensure you have Python 3.8+ and pip installed.

2. Clone the Repository
git clone [https://github.com/Shantralee-58/alx-project-nexus.git](https://github.com/Shantralee-58/alx-project-nexus.git)
cd alx-project-nexus

3. Setup Virtual Environment
Create and activate a virtual environment to isolate project dependencies.

python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate

4. Installation
Install all required Python dependencies from the requirements.txt file:

pip install -r requirements.txt

5. Database Setup & Initialization
Apply migrations and create the necessary database schema:

python manage.py makemigrations
python manage.py migrate

To access the Django Admin or to test authenticated features, create a superuser:

python manage.py createsuperuser

6. Run the Application
Start the local development server:

python manage.py runserver

The application will be accessible in your browser at: http://127.0.0.1:8000/

📂 Project Structure Overview
The project is divided into a core configuration and several distinct Django applications for modularity.

Root Directory (alx-project-nexus/)
File/Directory

Purpose

manage.py

Django's command-line utility.

requirements.txt

Lists all project dependencies.

.gitignore

Specifies files/folders Git ignores (venv, db.sqlite3).

static/

Global CSS, JavaScript, and image assets.

templates/

Shared base HTML template (base.html) and app-specific templates.

Core Applications
App Directory

Core Functionality

Key Files

products/

Product models, listing, API endpoints, and admin-only management.

models.py, api_views.py

orders/

Secure API for order creation/history, protected by authentication.

models.py, api_views.py, serializers.py

home/

The main landing page and primary site routing.

views.py, templates/home/

about/

Static pages (About Us) and contact form functionality.

views.py (handles email sending), contact_us.html

stores/

Manages and displays static store location data.

models.py, views.py

sustainify/

The core project configuration, settings, and root URL routing.

settings.py, urls.py

🔒 Key Features & API
Implemented Features
User Authentication: Full user registration, login, and secure session management.

Catalog Management: CRUD functionality for products and categories (via Django Admin).

Secure Ordering: Users can place complex orders via a protected API endpoint.

Order Tracking: Authenticated users can view their past orders via the web interface.

Contact Functionality: A working contact form that simulates sending an email (outputs to the console).

Responsive Design: Header and main content adjust for mobile and desktop screens.

API Endpoints (Django REST Framework)
All authenticated endpoints use token-based authentication (e.g., Token <hash>).

Endpoint

Method

Description

Authentication

/api/products/

GET

List and filter products.

Optional

/api/orders/

POST

Place a new order (requires product_id and quantity).

Required

/api/orders/

GET

List orders placed by the authenticated user.

Required

/api/products/{id}/

PUT/POST/DELETE

Modify product data.

Admin Only

Example Order Placement
To place an order, send a POST request to /api/orders/ with the following JSON payload:

{
    "items": [
        {
            "product_id": 1,
            "quantity": 2
        },
        {
            "product_id": 5,
            "quantity": 1
        }
    ]
}

Note: The API logic automatically calculates the total cost, checks stock, and assigns the order to the authenticated user.
