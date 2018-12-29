from app.models import Category, Item, User, db

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from loremipsum import get_sentences

lorem = str((get_sentences(1)))

db.create_all()

# Clears all data in database
db.session.query(User).delete()
db.session.query(Category).delete()
db.session.query(Item).delete()
db.session.commit()

# Category data
HoodiesCat = Category(name='Hoodies', description=lorem)
db.session.add(HoodiesCat)
PantsCat = Category(name='Pants', description=lorem)
db.session.add(PantsCat)
ShirtsCat = Category(name='Shirts', description=lorem)
db.session.add(ShirtsCat)
ShoesCat = Category(name='Shoes', description=lorem)
db.session.add(ShoesCat)
SocksCat = Category(name='Socks', description=lorem)
db.session.add(SocksCat)
AccCat = Category(name='Accessories', description=lorem)
db.session.add(AccCat)
db.session.commit()

# Item data
hoodies = ['Black-Hoodie', 'White-Hoodie', 'Red-Hoodie', 'Heart-Hoodie']
for hoodie in hoodies:
    item = Item(style=hoodie, category=HoodiesCat, description=lorem)
db.session.add(item)
db.session.commit()

pants = ['TheSkinny', 'TheChino', 'Shorts', 'Jeans']
for pant in pants:
    item = Item(style=pant, category=PantsCat, description=lorem)
db.session.add(item)
db.session.commit()

shirts = ['Button-up', 'ShortSleeve', 'LongSleeve', 'Golf']
for shirt in shirts:
    item = Item(style=shirt, category=ShirtsCat, description=lorem)
db.session.add(item)
db.session.commit()

shoes = ['Sneaker', 'Runner', 'Boot']
for shoe in shoes:
    item = Item(style=shoe, category=ShoesCat, description=lorem)
db.session.add(item)
db.session.commit()

socks = ['Casual', 'Formal', 'Hiking']
for sock in socks:
    item = Item(style=sock, category=SocksCat, description=lorem)
db.session.add(item)
db.session.commit()

accessories = ['Necklace', 'Rings', 'Glasses']
for accessory in accessories:
    item = Item(style=accessory, category=AccCat, description=lorem)
db.session.add(item)
db.session.commit()

print ('Categories and items added to database!')