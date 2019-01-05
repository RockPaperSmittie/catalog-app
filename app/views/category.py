from flask import Blueprint, render_template
from sqlalchemy import asc, desc
from app.models.models import Category, Item, db

category = Blueprint('category', __name__)

@category.route("/")
@category.route("/catalog")
def show_categories():
    """Show Categories on homescreen."""
    categories = db.session.query(Category).order_by(db.asc(Category.name)).all()
    return render_template('categories.html', categories=categories, category = category)
