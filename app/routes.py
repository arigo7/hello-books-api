from app import db
from flask import Blueprint
from .models.book import Book
from flask import request
from flask import jsonify

books_bp = Blueprint("books", __name__, url_prefix="/books")

@books_bp.route("/<book_id>", methods=["GET"], strict_slashes = False)
def handle_single_book(book_id):
    # try to find the book with the given id
    book = Book.query.get(book_id)
    if book: 
        return {
            "id": book.id,
            "title": book.title,
            "description": book.description
            }, 200
    # if falsy
    return {"success": False,
            "message": f"Book #{book_id} was not found"
            }, 404

@books_bp.route("", methods = ["POST", "GET"], strict_slashes = False)
def handle_books():
    if request.method == "GET":
        books = Book.query.all()
        books_response = []
        for book in books:
            books_response.append({
                "id": book.id,
                "title": book.title,
                "description": book.description
            })
        return jsonify(books_response), 200
    else:
        request_body = request.get_json()
    new_book = Book(title = request_body["title"],
                    description = request_body["description"])

    db.session.add(new_book) # "adds model to the db"
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
