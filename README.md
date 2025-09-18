# Sustainify 🌱

**Developer:** Idah Lindiwe Khumalo  
**Location:** City of Johannesburg, Gauteng, South Africa  
**Contact:** +27671114441 / +27780542966 / +27768338122  
**Email:** lindiwekhumalo833@gmail.com  
**LinkedIn:** [https://www.linkedin.com/in/idah-khumalo-765778159](https://www.linkedin.com/in/idah-khumalo-765778159)  
**GitHub:** [https://github.com/Shantralee-58](https://github.com/Shantralee-58)  

---

## Project Description

Sustainify is an eco-conscious e-commerce and service platform designed to connect users with sustainable products and services. Users can buy eco-friendly products, track eco-scores, create swap listings, and receive notifications about relevant items. Sustainify emphasizes sustainability, user empowerment, and ethical consumption.

---

## Project Structure

```
alx-project-nexus/
├── sustainify/                # Django project settings
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── products/                  # Product management app
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── users/                     # User management app
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── orders/                    # Order management app
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── ERD/                       # PlantUML ERD files
├── manage.py
├── requirements.txt
└── README.md

--------
```
## ERD Diagram

![Sustainify ERD](ERD/sustainify_erd.png)

-----

## Tech Stack

Backend: Django 5.2.6 (Python 3.12)

Frontend: HTML, CSS, JavaScript 

Database: SQLite (dev) / PostgreSQL (prod)

Authentication: Custom User Model, hashed passwords, CSRF protection

Tools: Git, PlantUML, venv

## Features

User registration & login

CRUD for products, stores, orders

Category-based product classification

Order & order item tracking

EcoScore tracking

Swap listings for products

Notifications system

Responsive UI

## Setup Instructions

git clone https://github.com/Shantralee-58/alx-project-nexus.git
cd alx-project-nexus
python -m venv venv

# Windows
source venv/Scripts/activate

# macOS/Linux
source venv/bin/activate

pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser  # optional
python manage.py runserver
Open in browser: http://127.0.0.1:8000/

