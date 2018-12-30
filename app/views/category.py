from flask import Blueprint, render_template
from sqlalchemy import asc, desc
from app.models import Category, Item, db
from database import session

category = Blueprint('category', __name__)

@category.route("/")
@category.route("/catalog")
def show_categories():
    """Show all current categories with the latest added items."""
    categories = db.session.query(Category).order_by(asc(Category.name)).all()
    items = db.session.query(Item).order_by(desc(Item.created_date)).limit(10).all()
    output = ''
    for i in items:
        output += i.category
        output += '</br>'
        output += i.style
        output += '</br>'
    
    return output