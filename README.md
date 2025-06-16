# 🍕 Pizza Restaurant API - Flask Backend

This project is a RESTful API for managing **restaurants**, **pizzas**, and the many-to-many relationship between them using **RestaurantPizzas**. It's built using **Flask**, **SQLAlchemy**, and follows the **MVC (Model-View-Controller)** design pattern.

---

## 📁 Project Purpose

The goal of this challenge is to:
- Build a backend Flask API from scratch
- Practice relational data modeling
- Implement CRUD operations and validation
- Test API endpoints using Postman
- Structure code using MVC for better organization

---

## 🧱 Tech Stack

- **Flask**: Lightweight web framework for Python
- **Flask SQLAlchemy**: ORM for managing database models
- **Flask Migrate**: For handling database migrations
- **SQLite**: Local database
- **Postman**: For testing endpoints

---

## ⚙️ Setup Instructions

```bash
# Install dependencies
pipenv install flask flask_sqlalchemy flask_migrate
pipenv shell

# Set environment variable
export FLASK_APP=server/app.py

# Database setup
flask db init
flask db migrate -m "Initial migration"
flask db upgrade

# Seed database with test data
python -m server.seed

🏗 Project Structure (MVC)

server/
├── app.py                     # App factory that initializes Flask, DB, and Blueprints
├── config.py                  # Configuration settings
├── seed.py                    # Script to populate test data
├── models/
│   ├── restaurant.py          # Restaurant model
│   ├── pizza.py               # Pizza model
│   └── restaurant_pizza.py    # Join table with price validation
├── controllers/
│   ├── restaurant_controller.py       # Handles /restaurants routes
│   ├── pizza_controller.py            # Handles /pizzas routes
│   └── restaurant_pizza_controller.py # Handles /restaurant_pizzas

🔄 Models Explained
🏪 Restaurant

    Fields: id, name, address

    Relationships: Has many restaurant_pizzas

🍕 Pizza

    Fields: id, name, ingredients

    Relationships: Has many restaurant_pizzas

💰 RestaurantPizza (Join Table)

    Fields: id, price, restaurant_id, pizza_id

    Relationships: Belongs to a restaurant and a pizza

    Validation: Price must be between 1 and 30

    Enforces cascading delete: If a restaurant is deleted, associated restaurant_pizzas are also removed.

🔁 API Routes Overview
GET /restaurants

    Returns all restaurants

GET /restaurants/<id>

    Returns a specific restaurant and its pizzas

    Returns 404 if not found

DELETE /restaurants/<id>

    Deletes a restaurant and associated restaurant_pizzas

    Returns 204 No Content on success

GET /pizzas

    Returns all pizzas

POST /restaurant_pizzas

    Creates a new RestaurantPizza entry

    Validates that price is between 1 and 30

    Returns associated pizza and restaurant data on success

    Returns 400 with error message on failure

✅ Example Request & Response
POST /restaurant_pizzas

Request:

{
  "price": 15,
  "pizza_id": 1,
  "restaurant_id": 2
}

Response:

{
  "id": 4,
  "price": 15,
  "pizza": {
    "id": 1,
    "name": "Pepperoni",
    "ingredients": "Dough, Tomato Sauce, Cheese, Pepperoni"
  },
  "restaurant": {
    "id": 2,
    "name": "Mama's Pizza",
    "address": "123 Main St"
  }
}

🧪 Testing the API (Postman)

    Open Postman

    Click Import

    Select challenge-1-pizzas.postman_collection.json

    Test each endpoint: GET, POST, DELETE

🧾 Summary

This project demonstrates:

    How to build a backend API using Flask

    Setting up models with relationships and validations

    Structuring a clean MVC codebase

    Testing endpoints with Postman

    Properly documenting a backend project

👤 Author

Leparan Felix
GitHub: @leparan-felix