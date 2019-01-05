@item.route("/catalog/<path:category_name>")
@item.route("/catalog/<path:category_name>/items")
def show_items(category_name):
    """Show a category and all of his items."""
    categories = db.session.query(Category).order_by(db.asc(Category.name)).all()
    category = db.session.query(Category).filter_by(name=category_name).one_or_none()
    items = db.session.query(Item).filter_by(category_id=category.id).all()
    return render_template('show_item.html, categories=categories')