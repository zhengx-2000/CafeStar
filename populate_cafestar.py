import os
import numpy as np

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'cafe_star_project.settings')

import django

django.setup()

from CafeStar.models import User, Drink, Order, ShopStatus


def populate():
    drinks = [
        {'DrinkID': 0,
         'Name': 'Latte',
         'Picture': open('static/image/Latte.png', 'r'),
         'Description': 'This is Latte',
         'Nutrition': 'This is nutrition for Latte',
         'Ingredients': 'This is ingredients for Latte',
         'Price': 20,
         'Point': 2,
         'Rating': 5, },
    ]

    orders = [
        {'OrderID': 1,
         'UserID': 0,
         'DrinkID': 0,
         'Status': False,
         'Drink': 'Latte',
         'Sweetness': 'Sweet',
         'Milk': 'Milk',
         'PickupTime': '12:00',
         'Price': 20,
         'Point': 2, }
    ]

    users = [
        {'UserID': 0,
         'Manager': False,
         'Fullname': 'John',
         'Username': 'IT',
         'Email': '12345678J@student.gla.ac.uk',
         'Password': '123456',
         'PhoneNumber': '12345654321',
         'Point': 0, }
    ]

    for drink in drinks:
        add_drink(drink)
    for order in orders:
        add_order(order)
    for user in users:
        add_user(user)


def add_drink(drink):
    d = Drink.objects.get_or_create(DrinkID=drink['DrinkID'])[0]
    d.Name = drink['Name']
    d.Picture = drink['Picture']
    d.Description = drink['Description']
    d.Nutrition = drink['Nutrition']
    d.Ingredients = drink['Ingredients']
    d.Price = drink['Price']
    d.Point = drink['Point']
    d.Rating = drink['Rating']
    d.save()
    print('drink saved')
    return d


def add_order(order):
    o = Order.objects.get_or_create(OrderID=order['OrderID'],
                                    UserID=order['UserID'],
                                    DrinkID=order['DrinkID'],
                                    Status=order['Status'],
                                    Drink=order['Drink'],
                                    Sweetness=order['Sweetness'],
                                    Milk=order['Milk'],
                                    PickupTime=order['PickupTime'],
                                    Price=order['Price'],
                                    Point=order['Point'])[0]
    o.save()
    print('order saved')
    return o


def add_user(user):
    u = User.objects.get_or_create(UserID=user['UserID'],
                                   Manager=user['Manager'],
                                   Fullname=user['Fullname'],
                                   Username=user['Username'],
                                   Email=user['Email'],
                                   Password=user['Password'],
                                   PhoneNumber=user['PhoneNumber'],
                                   Point=user['Point'])[0]
    u.save()
    print('user saved')
    return u


# Start execution here!
if __name__ == '__main__':
    print('Starting CafeStar population script...')
    populate()
