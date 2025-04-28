from flask import Blueprint, jsonify, request
from .models import (fetch_all_loans, fetch_loan_by_id, insert_loan, update_loan_info, delete_loan_by_id)

bp = Blueprint('loan_routes', __name__)

@bp.route('/loans', methods=['GET'])
def get_loans():
    loans = fetch_all_loans()
    if loans:
        return jsonify(loans), 200
    return jsonify({"message": "No loans found"}), 404

@bp.route('/loan/<int:id>', methods=['GET'])
def get_loan_by_id(id):
    loan = fetch_loan_by_id(id)
    if loan:
        return jsonify(loan), 200
    return jsonify({"error": "Loan not found"}), 404

@bp.route('/create_loan', methods=['POST'])
def create_loan():
    data = request.get_json()
    user_id = data.get('user_id')
    book_id = data.get('book_id')
    tanggal_pinjam = data.get('tanggal_pinjam')
    tanggal_kembali = data.get('tanggal_kembali')
    status = data.get('status')

    if not all([user_id, book_id, tanggal_pinjam, tanggal_kembali, status]):
        return jsonify({"error": "user_id, book_id, tanggal_pinjam, tanggal_kembali, status are required"}), 400

    loan_id = insert_loan(user_id, book_id, tanggal_pinjam, tanggal_kembali, status)
    return jsonify({
        "id": loan_id,
        "user_id": user_id,
        "book_id": book_id,
        "tanggal_pinjam": tanggal_pinjam,
        "tanggal_kembali": tanggal_kembali,
        "status": status
    }), 201

@bp.route('/update_loan/<int:id>', methods=['PUT'])
def update_loan(id):
    data = request.get_json()
    user_id = data.get('user_id')
    book_id = data.get('book_id')
    tanggal_pinjam = data.get('tanggal_pinjam')
    tanggal_kembali = data.get('tanggal_kembali')
    status = data.get('status')

    if not all([user_id, book_id, tanggal_pinjam, tanggal_kembali, status]):
        return jsonify({"error": "user_id, book_id, tanggal_pinjam, tanggal_kembali, status are required"}), 400

    loan = fetch_loan_by_id(id)
    if not loan:
        return jsonify({"error": "Loan not found"}), 404

    update_loan_info(id, user_id, book_id, tanggal_pinjam, tanggal_kembali, status)
    return jsonify({
        "id": id,
        "user_id": user_id,
        "book_id": book_id,
        "tanggal_pinjam": tanggal_pinjam,
        "tanggal_kembali": tanggal_kembali,
        "status": status
    }), 200

@bp.route('/delete_loan/<int:id>', methods=['DELETE'])
def delete_loan(id):
    loan = fetch_loan_by_id(id)
    if not loan:
        return jsonify({"error": "Loan not found"}), 404

    delete_loan_by_id(id)
    return jsonify({"message": f"Loan with id {id} deleted"}), 200
