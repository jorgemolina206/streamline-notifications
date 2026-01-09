from app.database.db import db

class Preference(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("user.id", ondelete="CASCADE"),
        nullable=False,
        unique=True
    )

    email_enabled = db.Column(db.Boolean, default=True)
    push_enabled = db.Column(db.Boolean, default=False)

    quiet_hours_start = db.Column(db.Integer, default=22)
    quiet_hours_end = db.Column(db.Integer, default=7)

    user = db.relationship("User", back_populates="preference")
