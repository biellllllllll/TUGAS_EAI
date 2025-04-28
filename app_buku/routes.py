from flask import Blueprint, jsonify, request
from .models import (fetch_all_books, fetch_book_by_id, insert_book, update_book_info, delete_book_by_id)

bp = Blueprint('book_routes', __name__)

@bp.route('/books', methods=['GET'])
def get_books():
    books = fetch_all_books()
    if books:
        return jsonify(books), 200
    return jsonify({"message": "No books found"}), 404

@bp.route('/book/<int:id>', methods=['GET'])
def get_book_by_id(id):
    book = fetch_book_by_id(id)
    if book:
        return jsonify(book), 200
    return jsonify({"error": "Book not found"}), 404

@bp.route('/create_book', methods=['POST'])
def create_book():
    data = request.get_json()
    title = data.get('title')
    author = data.get('author')
    category = data.get('category')
    year = data.get('year')

    if not all([title, author, category, year]):
        return jsonify({"error": "title, author, category, and year are required"}), 400

    book_id = insert_book(title, author, category, year)
    return jsonify({
        "id": book_id,
        "title": title,
        "author": author,
        "category": category,
        "year": year
    }), 201

@bp.route('/update_book/<int:id>', methods=['PUT'])
def update_book(id):
    data = request.get_json()
    title = data.get('title')
    author = data.get('author')
    category = data.get('category')
    year = data.get('year')

    if not all([title, author, category, year]):
        return jsonify({"error": "title, author, category, and year are required"}), 400

    book = fetch_book_by_id(id)
    if not book:
        return jsonify({"error": "Book not found"}), 404

    update_book_info(id, title, author, category, year)
    return jsonify({
        "id": id,
        "title": title,
        "author": author,
        "category": category,
        "year": year
    }), 200

@bp.route('/delete_book/<int:id>', methods=['DELETE'])
def delete_book(id):
    book = fetch_book_by_id(id)
    if not book:
        return jsonify({"error": "Book not found"}), 404

    delete_book_by_id(id)
    return jsonify({"message": f"Book with id {id} deleted"}), 200
