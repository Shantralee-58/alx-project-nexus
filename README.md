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

```text
alx-project-nexus/
├── sustainify/                # Django project settings
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── products/                  # Product management app
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
│
├── users/                     # User management app
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── orders/                    # Order management app
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
│
├── ERD/                       # PlantUML ERD files
├── manage.py
├── requirements.txt
└── README.md
ERD Diagram
PlantUML snippet for GitHub rendering:

plantuml
Copy code
@startuml Sustainify_ERD
skinparam linetype ortho
hide circle
skinparam classAttributeIconSize 0

class User {
  +id : UUID <<PK>>
  +email : varchar
  +username : varchar
  +password_hash : varchar
  +is_active : boolean
  +is_staff : boolean
  +role : varchar
  +created_at : timestamptz
}

class Store {
  +id : UUID <<PK>>
  +owner_id : UUID <<FK>>
  +name : varchar
  +description : text
  +location_lat : decimal
  +location_lng : decimal
  +created_at : timestamptz
}

class Product {
  +id : UUID <<PK>>
  +store_id : UUID <<FK>>
  +name : varchar
  +sku : varchar
  +description : text
  +price_cents : integer
  +quantity : integer
  +is_surplus : boolean
  +expiry_date : date
  +eco_category : varchar
  +created_at : timestamptz
}

class Category {
  +id : UUID <<PK>>
  +name : varchar
}

class ProductCategory {
  +id : UUID <<PK>>
  +product_id : UUID <<FK>>
  +category_id : UUID <<FK>>
}

class Order {
  +id : UUID <<PK>>
  +user_id : UUID <<FK>>
  +store_id : UUID <<FK>>
  +total_cents : integer
  +status : varchar
  +created_at : timestamptz
}

class OrderItem {
  +id : UUID <<PK>>
  +order_id : UUID <<FK>>
  +product_id : UUID <<FK>>
  +price_cents : integer
  +quantity : integer
}

class EcoScore {
  +id : UUID <<PK>>
  +user_id : UUID <<FK>>
  +score : integer
  +details : JSON
}

class SwapListing {
  +id : UUID <<PK>>
  +user_id : UUID <<FK>>
  +product_id : UUID <<FK>>
  +desired_items : text
  +status : varchar
  +created_at : timestamptz
}

class Notification {
  +id : UUID <<PK>>
  +user_id : UUID <<FK>>
  +type : varchar
  +payload : JSON
  +read : boolean
  +created_at : timestamptz
}

User "1" -- "0..*" Store : owns
Store "1" -- "0..*" Product : offers
Product "1" -- "0..*" ProductCategory : classified_as
Category "1" -- "0..*" ProductCategory : includes
User "1" -- "0..*" Order : places
Store "1" -- "0..*" Order : receives
Order "1" -- "0..*" OrderItem : contains
Product "1" -- "0..*" OrderItem : sold_as
User "1" -- "0..*" EcoScore : has
User "1" -- "0..*" SwapListing : creates
Product "1" -- "0..*" SwapListing : references
User "1" -- "0..*" Notification : receives

@enduml
You can render this ERD on GitHub using a PlantUML plugin or online PlantUML server.

Tech Stack
Backend: Django 5.2.6 (Python 3.12)

Frontend: HTML, CSS, JavaScript (colors: Green #2E8B57, Black, Creme White)

Database: SQLite (dev) / PostgreSQL (prod)

Authentication: Custom User Model, hashed passwords, CSRF protection

Tools: Git, PlantUML, venv

Features
User registration & login

CRUD for products, stores, orders

Category-based product classification

Order & order item tracking

EcoScore tracking

Swap listings for products

Notifications system

Responsive UI

Setup Instructions
Clone the repo:

bash
Copy code
git clone https://github.com/Shantralee-58/alx-project-nexus.git
cd alx-project-nexus
Create and activate virtual environment:

bash
Copy code
python -m venv venv
source venv/Scripts/activate   # Windows
# OR
source venv/bin/activate       # macOS/Linux
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Apply migrations:

bash
Copy code
python manage.py migrate
Create superuser (optional):

bash
Copy code
python manage.py createsuperuser
Run the development server:

bash
Copy code
python manage.py runserver
Open http://127.0.0.1:8000/ in browser.

Sustainify - Fully integrated eco-friendly e-commerce platform. 🌱

yaml
Copy code

