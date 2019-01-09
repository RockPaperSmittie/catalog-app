from flask import Blueprint, render_template
from sqlalchemy import asc, desc
from app.models.models import Category
from app.models.models import Item
from app import session

item = Blueprint('item', __name__)

@item.route("/catalog/<path:category_name>")
@item.route("/catalog/<path:category_name>/items")
def show_items(category_name):
    """Show a category and all of his items."""
    categories = session.query(Category).order_by(asc(Category.name)).all()
    category = session.query(Category).filter_by(name=category_name).one_or_none()
    items = session.query(Item).filter_by(category=category).all()
    return render_template('show_item.html', categories=categories, category=category, items=items)


@item.route("/catalog/<path:category_name>/<path:item_style>")
def show_item(category_name, item_style):
    """Show a category and all of his items."""
    category = session.query(Category).filter_by(name=category_name).one_or_none()
    item = session.query(Item).filter_by(category=category, style=item_style).one_or_none()
    return render_template('item_detail.html', category=category, item=item)