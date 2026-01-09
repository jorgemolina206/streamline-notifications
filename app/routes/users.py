from flask import Blueprint, request, jsonify
from app.database.db import db
from app.models.user import User

users_bp = Blueprint("users", __name__)
def is_valid_email(email: str) -> bool:
    if not isinstance(email, str):
        return False
    email = email.strip()
    if len(email) < 6 or len(email) > 255:
        return False
    if "@" not in email:
        return False
    local, _, domain = email.partition("@")
    if not local or "." not in domain:
        return False
    return True

@users_bp.post("/users")
def create_user():
    data = request.get_json() or {}
    email = data.get("email")

    if not is_valid_email(email):
        return jsonify({"error": "invalid email"}), 400

    if not email:
        return jsonify({"error": "email is required"}), 400

    if User.query.filter_by(email=email).first():
        return jsonify({"error": "email already exists"}), 409

    user = User(email=email)
    db.session.add(user)
    db.session.commit()

    return jsonify({"id": user.id, "email": user.email}), 201

@users_bp.get("/users/<int:user_id>")
def get_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "user not found"}), 404

    return jsonify({"id": user.id, "email": user.email})
