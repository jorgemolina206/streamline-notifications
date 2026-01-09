from flask import Blueprint, request, jsonify
from app.database.db import db
from app.models.preference import Preference

preferences_bp = Blueprint("preferences", __name__)

@preferences_bp.put("/users/<int:user_id>/preferences")
def upsert_preferences(user_id):
    data = request.get_json() or {}

    pref = Preference.query.filter_by(user_id=user_id).first()
    if not pref:
        pref = Preference(user_id=user_id)
        db.session.add(pref)

    if "email_enabled" in data:
        pref.email_enabled = bool(data["email_enabled"])
    if "push_enabled" in data:
        pref.push_enabled = bool(data["push_enabled"])
    if "quiet_hours_start" in data:
        pref.quiet_hours_start = int(data["quiet_hours_start"])
    if "quiet_hours_end" in data:
        pref.quiet_hours_end = int(data["quiet_hours_end"])

    db.session.commit()

    return jsonify({
        "user_id": pref.user_id,
        "email_enabled": pref.email_enabled,
        "push_enabled": pref.push_enabled,
        "quiet_hours_start": pref.quiet_hours_start,
        "quiet_hours_end": pref.quiet_hours_end
    })

@preferences_bp.get("/users/<int:user_id>/preferences")
def get_preferences(user_id):
    pref = Preference.query.filter_by(user_id=user_id).first()
    if not pref:
        return jsonify({"error": "preferences not found"}), 404

    return jsonify({
        "user_id": pref.user_id,
        "email_enabled": pref.email_enabled,
        "push_enabled": pref.push_enabled,
        "quiet_hours_start": pref.quiet_hours_start,
        "quiet_hours_end": pref.quiet_hours_end
    })
