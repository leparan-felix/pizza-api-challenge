from server.app import create_app, db
from server.models import Restaurant, Pizza, RestaurantPizza

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    p1 = Pizza(name='Emma', ingredients='Dough, Tomato Sauce, Cheese')
    p2 = Pizza(name='Diavola', ingredients='Tomato Sauce, Mozzarella, Spicy Salami')

    r1 = Restaurant(name="Mama's", address="123 Street")
    r2 = Restaurant(name="Kiki's Pizza", address="456 Street")

    db.session.add_all([p1, p2, r1, r2])
    db.session.commit()

    rp1 = RestaurantPizza(price=10, pizza_id=p1.id, restaurant_id=r1.id)
    rp2 = RestaurantPizza(price=12, pizza_id=p2.id, restaurant_id=r2.id)

    db.session.add_all([rp1, rp2])
    db.session.commit()
