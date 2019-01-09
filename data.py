from app.models.models import Category, Item, User
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from loremipsum import get_sentences
from app import session, create_tables

lorem = str((get_sentences(1)))

create_tables()

# Clears all data in database
session.query(User).delete()
session.query(Category).delete()
session.query(Item).delete()

session.commit()





# Category data
HoodiesCat = Category(name='Hoodies', description=lorem)
session.add(HoodiesCat)
PantsCat = Category(name='Pants', description=lorem)
session.add(PantsCat)
ShirtsCat = Category(name='Shirts', description=lorem)
session.add(ShirtsCat)
ShoesCat = Category(name='Shoes', description=lorem)
session.add(ShoesCat)
SocksCat = Category(name='Socks', description=lorem)
session.add(SocksCat)
AccCat = Category(name='Accessories', description=lorem)
session.add(AccCat)
session.commit()

# Item data

# session.add(Item(style='Black-Hoodie', 
# category=HoodiesCat, 
# description=lorem))
# session.add(Item(style='Red-Hoodie', 
# category=HoodiesCat, 
# description=lorem))

# session.commit()

hoodies = ['Black-Hoodie', 'White-Hoodie', 'Red-Hoodie', 'Heart-Hoodie']
for hoodie in hoodies:
    item = Item(style=hoodie, category=HoodiesCat, description=lorem)
    session.add(item)
    session.commit()
    print(item.style)

pants = ['TheSkinny', 'TheChino', 'Shorts', 'Jeans']
for pant in pants:
    item = Item(style=pant, category=PantsCat, description=lorem)
    session.add(item)
    session.commit()
    print(item.style)

shirts = ['Button-up', 'ShortSleeve', 'LongSleeve', 'Golf']
for shirt in shirts:
    item = Item(style=shirt, category=ShirtsCat, description=lorem)
    session.add(item)
    session.commit()
    print(item.style)

shoes = ['Sneaker', 'Runner', 'Boot']
for shoe in shoes:
    item = Item(style=shoe, category=ShoesCat, description=lorem)
    session.add(item)
    session.commit()
    print(item.style)

socks = ['Casual', 'Formal', 'Hiking']
for sock in socks:
    item = Item(style=sock, category=SocksCat, description=lorem)
    session.add(item)
    session.commit()
    print(item.style)

accessories = ['Necklace', 'Rings', 'Glasses']
for accessory in accessories:
    item = Item(style=accessory, category=AccCat, description=lorem)
    session.add(item)
    session.commit()
    print(item.style)

print ('Categories and items added to database!')

