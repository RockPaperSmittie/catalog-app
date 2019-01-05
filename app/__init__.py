from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from views.category import category
from app.models.models import Category, Item, User

app = Flask(__name__, instance_relative_config=True)
db = SQLAlchemy(app)

app.config.from_object('config')
app.config.from_pyfile('config.py')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.register_blueprint(category)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
    print('running on local server port 8000')
