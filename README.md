🚀 Setup Instructions

    Clone the repo and enter the project folder.

    Install dependencies with pipenv install.

    Activate environment: pipenv shell.

    Set Flask app: export FLASK_APP=server/app.py.

🗄️ Database Setup

    Run migrations:

        flask db init

        flask db migrate -m "Initial migration"

        flask db upgrade

    Seed database: python -m server.seed

📁 Project Structure (MVC)

    models/: SQLAlchemy models (restaurant.py, pizza.py, restaurant_pizza.py)

    controllers/: Flask route handlers

    app.py: App factory + blueprint registration

    seed.py: Seed data

    migrations/: Database version control

🔁 API Endpoints
🍽️ Restaurants

    GET /restaurants: List all restaurants

    GET /restaurants/<id>: Restaurant + pizzas

        404 if not found

    DELETE /restaurants/<id>: Delete restaurant + related restaurant_pizzas

        204 No Content if successful

🍕 Pizzas

    GET /pizzas: List all pizzas

➕ Restaurant Pizzas

    POST /restaurant_pizzas: Create a RestaurantPizza

        Validates price between 1–30

        Returns joined pizza and restaurant data

✅ Validations

    price in RestaurantPizza must be 1–30

    404 for missing restaurant/<id> routes

    Deleting a restaurant also deletes related records (cascading delete)

🧪 Testing with Postman

    Import challenge-1-pizzas.postman_collection.json into Postman

    Test all defined routes

📄 Submission Checklist

    ✅ MVC structure

    ✅ Models with validations

    ✅ All required routes

    ✅ Passing Postman tests

    ✅ Clear README.md
