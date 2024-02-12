# UMVC-Hub

## Project Structure

```
umvc_site/                    # Root project directory.
│
├── db.sqlite3                # Default SQLite database file.
│
├── manage.py                 # Command-line utility for administrative tasks.
│
├── umvc_site/                # Django project package (configuration and global settings).
│   ├── __init__.py
│   ├── asgi.py               # Entry-point for ASGI-compatible web servers.
│   ├── settings.py           # Project settings.
│   ├── urls.py               # Project URL declarations.
│   └── wsgi.py               # Entry-point for WSGI-compatible web servers.
│
├── webapp/                   # Main application directory.
│   ├── migrations/           # Database migrations directory.
│   │   └── __init__.py
│   ├── static/               # Directory for static files (CSS, JavaScript, images).
│   │   ├── css/
│   │   ├── js/
│   │   └── images/
│   ├── templates/            # Directory for HTML templates.
│   │   ├── base.html         # Base template.
│   │   ├── home.html
│   │   ├── vision.html
│   │   ├── history.html
│   │   ├── activities.html
│   │   ├── member_gallery.html
│   │   └── weekly_reports.html
│   ├── __init__.py
│   ├── admin.py              # Admin panel configuration.
│   ├── apps.py               # Application configuration.
│   ├── models.py             # Database models.
│   ├── tests.py              # Test cases.
│   ├── urls.py               # Application URL declarations.
│   └── views.py              # View functions.
│
├── users/                    # User authentication app (optional split for clarity).
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py             # User models, if custom user model is used.
│   ├── urls.py               # URL configurations related to user authentication.
│   └── views.py              # Views for login, logout, and registration.
│
└── requirements.txt          # File for listing project dependencies.

```