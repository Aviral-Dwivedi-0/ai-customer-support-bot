"""
AI Customer Support Bot - Server Startup Script
================================================

This script starts the Flask development server for the AI Customer Support Bot.
Run this file from the project root directory.

Usage:
    # From project root:
    python backend/run.py
    
    # Or navigate to backend first:
    cd backend
    python run.py
    
The server will start on http://localhost:5000
"""

import os
import sys

# Get the directory where run.py is located (backend directory)
backend_dir = os.path.dirname(os.path.abspath(__file__))

# Get the project root (parent of backend)
project_root = os.path.dirname(backend_dir)

# Add both to Python path to ensure imports work
sys.path.insert(0, backend_dir)
sys.path.insert(0, project_root)

# Change to backend directory so relative paths work correctly
os.chdir(backend_dir)

# Import and run the Flask app
from app.main import app

if __name__ == '__main__':
    print("\n" + "="*60)
    print("  AI Customer Support Bot - Backend Server")
    print("="*60)
    print(f"  Server starting at: http://localhost:5000")
    print(f"  Working directory: {os.getcwd()}")
    print(f"  Press Ctrl+C to stop the server")
    print("="*60 + "\n")
    
    # Run Flask development server
    # Use use_reloader=False to avoid path issues with reloader
    app.run(
        host='0.0.0.0',      # Accept connections from any IP
        port=5000,            # Default port
        debug=True,           # Enable debug mode for development
        use_reloader=False    # Disable reloader to avoid path issues
    )
