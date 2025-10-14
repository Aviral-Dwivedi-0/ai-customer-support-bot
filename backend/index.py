"""
AI Customer Support Bot - Vercel Entry Point
==============================================

This is the entry point for Vercel serverless deployment.
"""

import os
import sys

# Get the directory where this file is located
current_dir = os.path.dirname(os.path.abspath(__file__))

# Add to Python path
sys.path.insert(0, current_dir)

# Change to backend directory
os.chdir(current_dir)

# Import the Flask app
from app.main import app

# Export for Vercel
# Vercel will use this 'app' variable
if __name__ != '__main__':
    # For Vercel serverless
    application = app
