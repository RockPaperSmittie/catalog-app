from flask import Flask
# from views.about import about_blueprint
from app.views.category import category
from app.views.item import item
from app.views.authorization import auth
# from views.api import api

app = Flask(__name__, template_folder='app/templates')
app._static_folder = "app/static"

# Register all the blueprints.
# app.register_blueprint(about_blueprint)
app.register_blueprint(category)
app.register_blueprint(item)
app.register_blueprint(auth)
# app.register_blueprint(api)


if __name__ == "__main__":
    app.secret_key = "super_secret_key"
    app.run(host="0.0.0.0", port=5000, debug=True, threaded = False)