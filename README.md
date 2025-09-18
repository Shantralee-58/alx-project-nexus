# Sustainify 🌱

Sustainify is an eco-friendly marketplace and community platform designed to connect users, stores, and products with a focus on sustainability, responsible consumption, and surplus management. The application enables users to buy, sell, swap, and track eco-conscious products while rewarding eco-friendly behaviors with an EcoScore system.

---

## Features

- **User Management**
  - Custom registration with validation (username, password rules)
  - Role-based access: User, Store Owner, Admin
  - Profile and account management

- **Stores**
  - Users can create and manage stores
  - Stores have location, description, and owner

- **Products & Categories**
  - Eco-friendly products can be added to stores
  - Products can belong to multiple categories
  - Track surplus items, expiry dates, and eco-category

- **Orders & OrderItems**
  - Users can place orders from stores
  - Order details with items, price, and quantity

- **EcoScore**
  - Users earn scores based on eco-friendly actions
  - Track details in JSON format

- **SwapListings**
  - Users can list items for swap
  - Track desired items and listing status

- **Notifications**
  - Users receive notifications for orders, swaps, and updates

---

## Project Structure

alx-project-nexus/
├─ ERD/
│ └─ Sustainify_ERD.puml
├─ categories/
│ ├─ migrations/
│ └─ models.py
├─ orders/
│ ├─ migrations/
│ └─ models.py
├─ products/
│ ├─ migrations/
│ └─ models.py
├─ sustainify/
│ ├─ settings.py
│ ├─ urls.py
│ └─ wsgi.py
├─ users/
│ ├─ migrations/
│ ├─ models.py
│ ├─ views.py
│ ├─ urls.py
│ └─ forms.py
├─ venv/
├─ manage.py
└─ requirements.txt

@startuml Sustainify_ERD
' -----------------------------
' Sustainify ERD — Professional Version with Crow’s Foot
' -----------------------------
skinparam linetype ortho
hide circle
skinparam classAttributeIconSize 0

' Entities
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

' Relationships with Crow's Foot Notation
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

Installation

Clone the repository

git clone https://github.com/Shantralee-58/alx-project-nexus.git
cd alx-project-nexus


Create and activate a virtual environment

python -m venv venv
source venv/Scripts/activate      # Windows
# or
source venv/bin/activate          # Mac/Linux


Install dependencies

pip install -r requirements.txt


Apply migrations

python manage.py migrate


Create a superuser (admin)

python manage.py createsuperuser


Run the development server

python manage.py runserver


Access the app

Frontend: http://127.0.0.1:8000/

Admin Panel: http://127.0.0.1:8000/admin/

License

This project is MIT Licensed — see LICENSE for details.

Contact

Developer: Idah Lindiwe Khumalo

Email: lindiwekhumalo833@gmail.com

GitHub: https://github.com/Shantralee-58

LinkedIn: https://www.linkedin.com/in/idah-khumalo-765778159
