from app import db
from flask import Blueprint
from .models.book import Book
from flask import request
from flask import jsonify # optional

books_bp = Blueprint("books", __name__, url_prefix="/books")

@books_bp.route("/<book_id>", methods=["DELETE"])
def delete_book(book_id):
    book = Book.query.get(book_id)
    # form_data = request.get_json() # save user input form_data as json format 
    # book.title = form_data["title"] # updating model? title fieldlanguage?
    # book.description = form_data["description"] # updating model description field for book = book_id
    db.session.delete(book)
    db.session.commit()
    return {"success": True,
            "message": f"Book #{book.id}, successfully deleted"
            }, 201

@books_bp.route("/<book_id>", methods=["PUT"])
def update_book(book_id):
    book = Book.query.get(book_id)
    form_data = request.get_json() # save user input form_data as json format 
    book.title = form_data["title"] # updating model? title fieldlanguage?
    book.description = form_data["description"] # updating model description field for book = book_id
    db.session.commit()

    return {"success": True,
            "message": f"Book #{book.id}, successfully updated"
            }, 201

@books_bp.route("/<book_id>", methods=["GET"], strict_slashes = False)
def handle_single_book(book_id):
    # try to find the book with the given id
    book = Book.query.get(book_id)
    if book: # successful getting of the single book
        return {
            "id": book.id,
            "title": book.title,
            "description": book.description
            }, 200
    # if falsy - this is the response
    return {"success": False,
            "message": f"Book #{book_id} was not found"
            }, 404

@books_bp.route("", methods = ["POST", "GET"], strict_slashes = False)
def handle_books():
    if request.method == "GET":
        books = Book.query.all()  # this is a list
        books_response = []
        for book in books:
            books_response.append({
                "id": book.id,
                "title": book.title,
                "description": book.description
            })
        return jsonify(books_response), 200  # you see this in POSTMAN
    else: # for POST
        request_body = request.get_json()
        new_book = Book(title = request_body["title"],
                    description = request_body["description"])

    db.session.add(new_book) # "adds model to the db" - (like git commit)
    db.session.commit() # does the action above
    # return (f"Book #{new_book.title} has been created", 201)
    return {"success": True,
            "message": f"Book #{new_book.title} has been created"
            }, 201

# hello_world_bp = Blueprint("hello_world", __name__)

# @hello_world_bp.route('/hello-world', methods=["GET"])
# def get_hello_world():
#     my_response = "Hello, World!"
#     return my_response

# @hello_world_bp.route('/hello-world/JSON', methods=["GET"])
# def hello_world_json():
#     return{ "name": "AriGO",
#     "message": "Hola",
#     "hobbies": ["hiking", "biking", "coding", "potery"] }, 201


# @hello_world_bp.route("/broken-endpoint-with-broken-server-code")
# def broken_endpoint():
#     response_body = {
#         "name": "Ada Lovelace",
#         "message": "Hello!",
#         "hobbies": ["Fishing", "Swimming", "Watching Reality Shows"]
#     }
#     new_hobby = "Surfing"
#     response_body["hobbies"].append(new_hobby)
#     return response_body
