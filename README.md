Streamline Notifications

Overview
A backend service that manages user notification preferences and generates notifications from streaming events.

Features
- Create and fetch users
- Store notification preferences per user
- Ingest events like stream_live and new_follower
- Generate and store notifications in SQLite
- List recent notification history
- Basic automated test coverage with pytest

Tech stack
- Python
- Flask
- Flask-SQLAlchemy
- SQLite
- pytest

Run locally
1) Create venv and activate
python3 -m venv .venv
source .venv/bin/activate

2) Install dependencies
pip install -r requirements.txt

3) Run the server
python run.py

Endpoints
GET /api/health
POST /api/users
GET /api/users/<user_id>
PUT /api/users/<user_id>/preferences
GET /api/users/<user_id>/preferences
POST /api/events
GET /api/users/<user_id>/notifications

Example flow
1) Create user
curl -X POST http://127.0.0.1:5000/api/users \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com"}'

2) Set preferences
curl -X PUT http://127.0.0.1:5000/api/users/1/preferences \
  -H "Content-Type: application/json" \
  -d '{"email_enabled":true,"push_enabled":false,"quiet_hours_start":22,"quiet_hours_end":7}'

3) Post event
curl -X POST http://127.0.0.1:5000/api/events \
  -H "Content-Type: application/json" \
  -d '{"user_id":1,"event_type":"stream_live","payload":{"channel":"MyChannel"}}'

4) List notifications
curl http://127.0.0.1:5000/api/users/1/notifications

Tests
pytest
