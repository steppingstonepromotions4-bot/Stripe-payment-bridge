"""WSGI entry point for Gunicorn.

Exposes the Flask application object as `application` for WSGI servers.

NOTE: Normally you would keep this file OUTSIDE the virtual environment.
It currently lives in `venv/` only because of your deployment request.
Consider moving `app.py` and `wsgi.py` to the project root later.
"""

import os
import sys

# Ensure the directory containing app.py is on sys.path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from app import app as application  # Flask instance from app.py

if __name__ == "__main__":
    # Local debug run (not used by Gunicorn in production)
    application.run(host="127.0.0.1", port=5000, debug=True)
