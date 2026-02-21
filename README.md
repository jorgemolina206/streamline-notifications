
# Streamline Notifications

## Overview
Streamline Notifications is a backend service that manages user notification preferences and generates notifications from streaming events.

This project demonstrates backend API development with Python/Flask, relational data modeling, and test coverage with pytest.

---

## Features
- Create and fetch users
- Store notification preferences per user
- Ingest events like `stream_live` and `new_follower`
- Generate and store notifications in SQLite
- List recent notification history
- Basic automated test coverage with pytest

---

## Tech Stack
- Python
- Flask
- Flask-SQLAlchemy
- SQLite
- pytest

---

## Run Locally

1) Create and activate virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate

2) Install dependencies

pip install -r requirements.txt

3) Run the server

python run.py

───

API Endpoints

• GET /api/health
• POST /api/users
• GET /api/users/<user_id>
• PUT /api/users/<user_id>/preferences
• GET /api/users/<user_id>/preferences
• POST /api/events
• GET /api/users/<user_id>/notifications

───

Example Flow

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

Bash
curl http://127.0.0.1:5000/api/users/1/notifications

───

Run Tests

pytest

───

Future Improvements

• Add authentication/authorization
• Expand automated test coverage
• Add Docker setup
• Add CI workflow for tests

───

Author

Jorge Molina
GitHub: github.com/jorgemolina206
