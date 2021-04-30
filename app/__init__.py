from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate 

db = SQLAlchemy()
migrate = Migrate()

# he used ada_books_develovement vs hello_books_development
# postgresql+psycopg2://postgres:postgres@localhost:5432/hello_books_development
def create_app(test_config=None):
    app = Flask(__name__)

    # DB Configuration - here I give it my connection string
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://postgres:postgres@localhost:5432/hello_books_development"

    # initializing my sqlalchemy object - telling it this is the app to 
    # work with - 
    db.init_app(app)  
    migrate.init_app(app, db) # app to work with, this is the way to get to the db

    from app.models.book import Book  # this makes it visible - we have to import
    # our models this way before we start doing anything with the API
    # - We want to do the import after we configure the database stuff - after it's 
    # already connected to the db
    # if we design more models, we'll import new models here too

    from .routes import hello_world_bp
    app.register_blueprint(hello_world_bp)
    return app
