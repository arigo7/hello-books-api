from app import db

#its named Book because SQLAlchemy likes singular table names. 
# I could rename it with __tablename__ = "books"
class Book(db.Model): # an instance of SQLAlchemy
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    # __tablename__ = "books"  #if I don't have this, it'll link it
    # to a table with the name of the class

    def to_string(self):
        return f"{self.id}: {self.title} Description: {self.description}" 