from app.database.db import db
from app.models.notification import Notification
from app.models.preference import Preference

def create_notification(user_id, event_type, message):
    pref = Preference.query.filter_by(user_id=user_id).first()

    if pref and pref.email_enabled is False and pref.push_enabled is False:
        return None

    n = Notification(
        user_id=user_id,
        event_type=event_type,
        message=message,
        status="queued"
    )
    db.session.add(n)
    db.session.commit()
    return n
