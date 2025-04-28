from flask import Blueprint, jsonify, request
from .models import (fetch_all_users, insert_user,update_user_name, fetch_user_by_id,delete_user_by_id)

bp = Blueprint('user_routes', __name__)

@bp.route('/users', methods=['GET'])
def get_users():
    users = fetch_all_users()
    return jsonify(users), 200

@bp.route('/users/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    user = fetch_user_by_id(user_id)
    if user:
        return jsonify(user), 200
    else:
        return jsonify({"error": "User not found"}), 404

@bp.route('/create_user', methods=['POST'])
def create_user():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    
    if not name:
        return jsonify({"error": "name is required"}), 400
    if not email:
        return jsonify({"error": "email is required"}), 400
    
    user_id = insert_user(name, email)
    return jsonify({"id": user_id, "name": name, "email": email}), 201

@bp.route('/update_user/<int:id>', methods=['PUT'])
def update_user(id):
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    
    if not name:
        return jsonify({"error": "name is required"}), 400
    if not email:
        return jsonify({"error": "email is required"}), 400
    
    user = fetch_user_by_id(id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    
    update_user_name(id, name, email)
    return jsonify({"id": id, "name": name, "email": email}), 200

@bp.route('/delete_user/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = fetch_user_by_id(id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    
    delete_user_by_id(id)
    return jsonify({"message": f"User with id {id} deleted successfully"}), 200
