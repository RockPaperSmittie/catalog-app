#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
from flask import Blueprint, render_template
from sqlalchemy import asc, desc
from app.models.models import Category
from app.models.models import Item
from app import session

category = Blueprint('category', __name__)

@category.route("/")
@category.route("/catalog")
def show_categories():
    """Show Categories on homescreen."""
    categories = session.query(Category).order_by(asc(Category.name)).all()
    return render_template('categories.html', categories=categories)