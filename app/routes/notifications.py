from flask import Blueprint, request, jsonify
from app.models.notification import Notification
from app.services.notification_service import create_notification
from app.services.event_service import format_message

notifications_bp = Blueprint("notifications", __name__)

@notifications_bp.post("/events")
def post_event():
    data = request.get_json() or {}
    user_id = data.get("user_id")
    event_type = data.get("event_type")
    payload = data.get("payload", {})

    if user_id is None or event_type is None:
        return jsonify({"error": "user_id and event_type are required"}), 400

    message = format_message(event_type, payload)
    n = create_notification(int(user_id), event_type, message)

    if not n:
        return jsonify({"status": "skipped"}), 200

    return jsonify({"notification_id": n.id, "status": n.status}), 201

@notifications_bp.get("/users/<int:user_id>/notifications")
def list_notifications(user_id):
    items = (
        Notification.query
        .filter_by(user_id=user_id)
        .order_by(Notification.id.desc())
        .limit(50)
        .all()
    )

    return jsonify([
        {
            "id": n.id,
            "event_type": n.event_type,
            "message": n.message,
            "status": n.status,
            "created_at": n.created_at.isoformat() if n.created_at else None
        }
        for n in items
    ])
