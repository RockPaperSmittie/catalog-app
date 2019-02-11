#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
from flask import Blueprint, jsonify
from app.models.models import Category, Item
from app import session
from sqlalchemy import asc

api = Blueprint('api', __name__)


@api.route("/catalog.json", methods=["GET"])
def get_categories():
    """Return all categories with their items."""
    categories = [c.serialize for c in session.query(Category).all()]
    for c in range(len(categories)):
        items = [
            i.serialize for i in session.query(Item).filter_by(
                category_id=categories[c]["id"]).all()]
        if items:
            categories[c]["Item"] = items
    return jsonify(Category=categories)


@api.route("/catalog/<path:category_name>.json", methods=["GET"])
def get_category(category_name):
    """Return a specific category with its items."""
    category = session.query(Category).filter_by(
        name=category_name).one_or_none()
    if category:
        category = category.serialize
        items = [
            i.serialize for i in session.query(Item).filter_by(
                category_id=category["id"]).all()]
        if items:
            category["Item"] = items
    return jsonify(Category=category)


@api.route(
    "/item/<path:category_name>/<path:item_style>.json", methods=["GET"])
def get_item(category_name, item_style):
    """Return a specific item."""
    category = session.query(Category).filter_by(
        name=category_name).one_or_none()
    if category:
        item = session.query(Item).filter_by(
            category_id=category.id, style=item_style).one_or_none()
        if item:
            return jsonify(Item=item.serialize)
    return jsonify(Item=none)
