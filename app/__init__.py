from flask import Flask
from app.config import Config
from app.database.db import db
from app.routes.health import health_bp
from app.routes.users import users_bp
from app.routes.preferences import preferences_bp
from app.routes.notifications import notifications_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    app.register_blueprint(health_bp, url_prefix="/api")
    app.register_blueprint(users_bp, url_prefix="/api")
    app.register_blueprint(preferences_bp, url_prefix="/api")
    app.register_blueprint(notifications_bp, url_prefix="/api")

    with app.app_context():
        db.create_all()

    return app
