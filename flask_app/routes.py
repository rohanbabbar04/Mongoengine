from flask import jsonify, request, Blueprint
from flask_app.model import Book

main = Blueprint('main', __name__)


@main.route("/books/createBook", methods=['POST'])
def create():
    bookID = request.json['bookID']
    name = request.json['name']
    author = request.json['author']
    price = request.json['price']
    book = Book(bookID=bookID, name=name, author=author, price=price)
    book.save()
    books = []
    for book in Book.objects():
        books.append(book.to_json())
    return jsonify(dict(books=books))


@main.route('/books')
def all_books():
    books = []
    print()
    for book in Book.objects():
        books.append(book.to_json())
    return jsonify(dict(books=books))


@main.route('/books/<int:bookID>/update', methods=['PUT'])
def update(bookID):
    name = request.json['name']
    author = request.json['author']
    price = request.json['price']
    book = Book.objects(bookID=bookID).first()
    book.update(name=name, author=author, price=price)
    return book.to_json()


@main.route('/books/<int:bookID>/delete', methods=['DELETE'])
def delete(bookID):
    book = Book.objects(bookID=bookID).first()
    book.delete()
    books = []
    for book in Book.objects():
        books.append(book.to_json())
    return jsonify(dict(books=books))
