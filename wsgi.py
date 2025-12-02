"""WSGI entry point for Gunicorn.

Gunicorn command: gunicorn wsgi:application
"""
import os
import stripe
from app import app as application

stripe.api_key = os.environ.get("STRIPE_SECRET_KEY")

if __name__ == "__main__":
    application.run(host="0.0.0.0", port=5000, debug=True)
