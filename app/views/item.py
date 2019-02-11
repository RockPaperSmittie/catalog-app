#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
from flask import Blueprint, render_template, request, redirect, flash, url_for
from flask import session as login_session
from sqlalchemy import asc, desc, exc
from app.models.models import Category
from app.models.models import Item
from app import session
from functools import wraps

item = Blueprint('item', __name__)


def login_required(f):
    """Decorator to redirect user if not logged."""
    @wraps(f)
    def wrapper(*args, **kwds):
        if "username" not in login_session:
            return redirect("/login")
        return f(*args, **kwds)
    return wrapper


@item.route("/catalog/<path:category_name>")
@item.route("/catalog/<path:category_name>/items")
def show_items(category_name):
    """Show a category and all of his items."""
    categories = session.query(Category).order_by(asc(Category.name)).all()
    category = session.query(Category).filter_by(
        name=category_name).one_or_none()
    items = session.query(Item).filter_by(category=category).all()
    return render_template(
        'show_item.html', categories=categories,
        category=category, items=items)


@item.route("/catalog/<path:category_name>/<path:item_style>")
def show_item(category_name, item_style):
    """Show a category and specific item."""
    category = session.query(
        Category).filter_by(name=category_name).one_or_none()
    item = session.query(Item).filter_by(
        category=category, style=item_style).one_or_none()
    return render_template('item_detail.html', category=category, item=item)


@item.route('/catalog/<path:category_name>/items/new', methods=['GET', 'POST'])
@login_required
def new_item(category_name):
    '''
    GET: Display Add Form
    POST: Create New Item
    '''
    category = session.query(
        Category).filter_by(name=category_name).one_or_none()

    if request.method == 'POST':
        newItem = Item()
        style = request.form['style'].strip()
        description = request.form['description'].strip()
        newItem = Item(
            style=style, description=description,
            category=category, user_id=login_session['user_id'])
        try:
            item = session.query(Item).filter_by(
                category=category, style=style).one_or_none()
            session.add(newItem)
            session.commit()
            flash("Item '{}' Successfully Added".format(
                newItem.style), "success")
            return redirect('/catalog')
        except exc.SQLAlchemyError:
                session.rollback()
                flash(
                    "You can not add this item since another item already "
                    " exists in the database with the same"
                    " style and category.")
                return redirect(
                    url_for("item.new_item", category_name=category.name))
    else:
        return render_template('new_item.html', category=category)


@item.route(
    '/catalog/<path:category_name>/<path:item_style>/edit',
    methods=['GET', 'POST'])
@login_required
def edit_item(category_name, item_style):
    category = session.query(
        Category).filter_by(name=category_name).one_or_none()
    item = session.query(Item).filter_by(style=item_style).one_or_none()
    if request.method == 'POST':
        if request.form['style']:
            item.style = request.form['style'].strip()
        if request.form['description']:
            item.description = request.form['description'].strip()
        session.add(item)
        session.commit()
        flash("Item '{}' Successfully Edited".format(item.style), "success")
        return redirect('/catalog')
    else:
        return render_template('edit_item.html', category=category, item=item)


@item.route(
    '/catalog/<path:category_name>/<path:item_style>/delete',
    methods=['GET', 'POST'])
@login_required
def delete_item(category_name, item_style):
    category = session.query(
        Category).filter_by(name=category_name).one_or_none()
    item = session.query(Item).filter_by(style=item_style).one_or_none()
    if request.method == 'POST':
        session.delete(item)
        session.commit()
        return redirect('/catalog')
    else:
        return render_template(
            'delete_item.html', category=category, item=item)
