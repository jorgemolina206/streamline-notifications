from app.database.db import db

class Notification(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("user.id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )

    event_type = db.Column(db.String(100), nullable=False)
    message = db.Column(db.String(500), nullable=False)

    status = db.Column(db.String(50), default="queued")
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    user = db.relationship("User", back_populates="notifications")
