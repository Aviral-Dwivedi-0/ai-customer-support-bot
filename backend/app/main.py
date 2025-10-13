"""
AI Customer Support Bot - Backend Server
=========================================

This Flask application provides a RESTful API for an AI-powered customer support chatbot.
It uses Google's Gemini AI model to answer customer questions based on FAQ content,
maintains conversation history in SQLite, and handles escalation to human agents.

Technology Stack:
    - Flask: Web framework for REST API
    - SQLite: Database for conversation persistence
    - Google Gemini AI: Natural language processing
    - CORS: Cross-origin resource sharing for frontend integration

Endpoints:
    - GET  /health    : Health check
    - POST /chat      : Main chat endpoint
    - POST /escalate  : Get conversation summary for escalation

Author: AI Customer Support Team
Date: October 2025
"""

import sqlite3
import os
import google.generativeai as genai
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

# ========== INITIALIZATION & CONFIGURATION ==========

# Load environment variables from .env file
load_dotenv()

# Configuration constants
# Paths are relative to the backend root directory
DATABASE = os.path.join('data', 'conversations.db')  # SQLite database file for conversation storage
FAQ_FILE = os.path.join('config', 'faqs.txt')        # Text file containing FAQ knowledge base

# Configure Gemini API
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
if not GEMINI_API_KEY:
    raise ValueError(
        "GEMINI_API_KEY not found in environment variables. "
        "Please create a .env file with your API key."
    )

# Initialize Gemini API with the API key
genai.configure(api_key=GEMINI_API_KEY)

# Configure Gemini model generation parameters
# - temperature: Controls randomness (0.0 = deterministic, 1.0 = creative)
# - top_p: Nucleus sampling threshold for token selection
# - top_k: Limits vocabulary to top k tokens
# - max_output_tokens: Maximum response length
generation_config = {
    "temperature": 0.7,        # Balanced creativity and consistency
    "top_p": 0.95,             # High diversity in responses
    "top_k": 40,               # Moderate vocabulary restriction
    "max_output_tokens": 1024, # ~750 words maximum response
}

# Initialize Gemini model with configuration
model = genai.GenerativeModel(
    model_name='gemini-2.5-flash',  # Fast, efficient model for customer support
    generation_config=generation_config
)

# Initialize Flask application
app = Flask(__name__)

# Enable CORS to allow frontend (React) to communicate with backend
# This allows requests from http://localhost:3000 (React dev server)
CORS(app)


# ========== DATABASE FUNCTIONS ==========

def init_db():
    """
    Initialize the SQLite database with conversations table.
    
    Creates a table to store conversation history with:
        - session_id: Unique identifier for each user session (PRIMARY KEY)
        - history: Text field storing the complete conversation history
    
    This function is idempotent - safe to call multiple times.
    Uses 'CREATE TABLE IF NOT EXISTS' to avoid errors on repeated calls.
    """
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    # Create conversations table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS conversations (
            session_id TEXT PRIMARY KEY,
            history TEXT
        )
    ''')
    
    conn.commit()
    conn.close()
    print("✅ Database initialized successfully")


def get_session_history(session_id):
    """
    Retrieve conversation history for a specific session.
    
    Args:
        session_id (str): Unique identifier for the user session
    
    Returns:
        str: Conversation history as text, or empty string if session not found
        
    Example:
        history = get_session_history("session_1234567890")
        # Returns: "User: Hello\nBot: Hi there!..."
    """
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    # Query for history matching the session_id
    cursor.execute(
        'SELECT history FROM conversations WHERE session_id = ?', 
        (session_id,)
    )
    result = cursor.fetchone()
    conn.close()
    
    # Return history if found, otherwise empty string
    return result[0] if result else ""


def save_session_history(session_id, history):
    """
    Save or update conversation history for a session.
    
    Uses INSERT OR REPLACE to handle both new sessions and updates
    to existing sessions in a single operation.
    
    Args:
        session_id (str): Unique identifier for the user session
        history (str): Complete conversation history to save
        
    Example:
        save_session_history(
            "session_1234567890",
            "User: Hello\nBot: Hi there!\nUser: Help me\nBot: Sure!"
        )
    """
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    # Insert new record or replace existing one
    cursor.execute('''
        INSERT OR REPLACE INTO conversations (session_id, history)
        VALUES (?, ?)
    ''', (session_id, history))
    
    conn.commit()
    conn.close()


# ========== FAQ FUNCTIONS ==========

def load_faqs():
    """
    Load FAQ content from text file.
    
    Reads the FAQ knowledge base from faqs.txt file.
    The FAQ file should contain question-answer pairs in the format:
        Q: Question text?
        A: Answer text.
    
    Returns:
        str: Complete FAQ content, or empty string if file not found
        
    Side effects:
        Prints loading status to console
    """
    if not os.path.exists(FAQ_FILE):
        print(f"❌ ERROR: {FAQ_FILE} not found")
        return ""
    
    # Read FAQ file with UTF-8 encoding to support special characters
    with open(FAQ_FILE, 'r', encoding='utf-8') as f:
        faqs_content = f.read()
    
    print(f"✅ Loaded {len(faqs_content)} characters from FAQs")
    return faqs_content


# Load FAQs at application startup (module level)
# This avoids re-reading the file on every request
FAQ_CONTENT = load_faqs()


# ========== GEMINI AI FUNCTIONS ==========

def call_gemini(prompt):
    """
    Call Google Gemini API with the given prompt.
    
    Sends a prompt to the Gemini AI model and returns the response.
    If any error occurs (API issues, network problems, etc.), returns
    "ESCALATE" to trigger human agent handoff.
    
    Args:
        prompt (str): The complete prompt to send to Gemini
    
    Returns:
        str: AI-generated response, or "ESCALATE" on error
        
    Raises:
        No exceptions - all errors are caught and logged
    """
    try:
        # Generate content using the configured model
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        # Log error and trigger escalation
        print(f"❌ Error calling Gemini API: {e}")
        return "ESCALATE"


def construct_prompt(user_query, history, faqs):
    """
    Construct the complete prompt for Gemini AI.
    
    Builds a structured prompt that includes:
        1. System instructions (role, rules)
        2. FAQ knowledge base
        3. Conversation history for context
        4. Current user question
    
    The prompt instructs the AI to:
        - Answer ONLY from FAQ content
        - Use conversation history for context
        - Return "ESCALATE" if answer not in FAQs
    
    Args:
        user_query (str): The user's current question
        history (str): Previous conversation history
        faqs (str): FAQ knowledge base content
    
    Returns:
        str: Complete formatted prompt ready for Gemini API
        
    Example:
        prompt = construct_prompt(
            "What's your return policy?",
            "User: Hello\nBot: Hi!",
            "Q: Return policy?\nA: 30 days..."
        )
    """
    prompt = f"""You are a helpful customer support assistant. Your job is to answer customer questions based ONLY on the FAQ information provided below.

IMPORTANT RULES:
1. If the answer to the question is found in the FAQs below, provide a helpful, friendly answer based on that information.
2. If the answer is NOT in the FAQs, respond with ONLY the word: ESCALATE
3. Be conversational and helpful when answering from the FAQs.
4. Use the conversation history to understand context.

FAQs:
{faqs}

Conversation History:
{history}

Customer Question: {user_query}

Your Answer:"""
    
    return prompt


def summarize_conversation(history):
    """
    Use Gemini AI to generate a conversation summary.
    
    Creates a concise summary of the conversation history for human agents.
    This helps agents quickly understand the context when taking over
    from the bot.
    
    Args:
        history (str): Complete conversation history
    
    Returns:
        str: AI-generated summary, or error message if summarization fails
        
    Example:
        summary = summarize_conversation(
            "User: What's shipping time?\nBot: 3-5 days..."
        )
        # Returns: "Customer asked about shipping times. Bot provided..."
    """
    # Handle empty history
    if not history.strip():
        return "No conversation history available."
    
    # Create summarization prompt
    summary_prompt = f"""Summarize the following customer support conversation concisely for a human agent:

{history}

Summary:"""
    
    try:
        # Generate summary using Gemini
        summary = call_gemini(summary_prompt)
        return summary
    except Exception as e:
        return f"Error generating summary: {e}"


# ========== FLASK API ENDPOINTS ==========

@app.route('/health', methods=['GET'])
def health():
    """
    Health check endpoint.
    
    Simple endpoint to verify the server is running and responsive.
    Used by monitoring tools and frontend to check backend status.
    
    Returns:
        JSON response with status "ok" and HTTP 200
        
    Example:
        GET http://localhost:5000/health
        Response: {"status": "ok"}
    """
    return jsonify({"status": "ok"}), 200


@app.route('/chat', methods=['POST'])
def chat():
    """
    Main chat endpoint for handling user messages.
    
    This endpoint orchestrates the complete conversation flow:
        1. Validate incoming request data
        2. Retrieve conversation history from database
        3. Construct AI prompt with FAQs and context
        4. Call Gemini AI for response
        5. Handle escalation if needed
        6. Update conversation history
        7. Return response to frontend
    
    Request Body (JSON):
        {
            "session_id": "unique_session_identifier",
            "query": "user's question text"
        }
    
    Response (JSON):
        Success: {"response": "bot's answer text"}
        Error: {"error": "error message"}, HTTP 400/500
        
    Error Handling:
        - 400: Missing required fields (session_id or query)
        - 500: Internal server error (database, API, etc.)
        
    Example:
        POST http://localhost:5000/chat
        Body: {"session_id": "session_123", "query": "What's your return policy?"}
        Response: {"response": "You can return products within 30 days..."}
    """
    try:
        # Parse JSON request body
        data = request.get_json()
        
        # Validate required fields
        if not data or 'session_id' not in data or 'query' not in data:
            return jsonify({
                "error": "Missing required fields: session_id or query"
            }), 400
        
        session_id = data['session_id']
        user_query = data['query']
        
        # Step 1: Retrieve conversation history from database
        history = get_session_history(session_id)
        
        # Step 2: Construct complete prompt with FAQs and context
        full_prompt = construct_prompt(user_query, history, FAQ_CONTENT)
        
        # Step 3: Call Gemini AI for response
        bot_response = call_gemini(full_prompt)
        
        # Step 4: Check if escalation is needed
        # If AI can't answer from FAQs, it returns "ESCALATE"
        if bot_response == "ESCALATE":
            # Generate conversation summary for human agent
            summary = summarize_conversation(history + f"\nUser: {user_query}")
            bot_response = (
                "I can't answer that question. I will escalate this to a human agent.\n\n"
                f"Summary for agent:\n{summary}"
            )
        
        # Step 5: Update conversation history in database
        new_history = history + f"\nUser: {user_query}\nBot: {bot_response}"
        save_session_history(session_id, new_history)
        
        # Step 6: Return bot response to frontend
        return jsonify({"response": bot_response})
    
    except Exception as e:
        # Log error and return 500 response
        print(f"❌ Error in /chat endpoint: {e}")
        return jsonify({"error": "Internal server error"}), 500


@app.route('/escalate', methods=['POST'])
def escalate():
    """
    Get conversation summary for escalation to human agent.
    
    This endpoint allows explicit escalation requests, returning
    a summarized version of the conversation for agent review.
    
    Request Body (JSON):
        {
            "session_id": "unique_session_identifier"
        }
    
    Response (JSON):
        Success: {"summary": "conversation summary text"}
        Error: {"error": "error message"}, HTTP 400/500
        
    Example:
        POST http://localhost:5000/escalate
        Body: {"session_id": "session_123"}
        Response: {"summary": "Customer asked about shipping and returns..."}
    """
    try:
        # Parse JSON request body
        data = request.get_json()
        
        # Validate required field
        if not data or 'session_id' not in data:
            return jsonify({"error": "Missing required field: session_id"}), 400
        
        session_id = data['session_id']
        
        # Retrieve conversation history
        history = get_session_history(session_id)
        
        # Generate summary using AI
        summary = summarize_conversation(history)
        
        # Return summary to caller
        return jsonify({"summary": summary})
    
    except Exception as e:
        # Log error and return 500 response
        print(f"❌ Error in /escalate endpoint: {e}")
        return jsonify({"error": str(e)}), 500


# ========== APPLICATION ENTRY POINT ==========

if __name__ == '__main__':
    """
    Application entry point.
    
    Initializes the database and starts the Flask development server.
    
    Server Configuration:
        - debug=True: Enable auto-reload on code changes and detailed error pages
        - host='0.0.0.0': Accept connections from any network interface
        - port=5000: Listen on port 5000 (standard Flask port)
    
    Note:
        This is for development only. For production, use a WSGI server
        like Gunicorn or uWSGI:
            gunicorn -w 4 -b 0.0.0.0:5000 app:app
    """
    # Initialize database tables
    init_db()
    
    # Print startup message
    print("=" * 60)
    print("🚀 AI Customer Support Bot - Backend Server")
    print("=" * 60)
    print(f"📡 Server running on: http://localhost:5000")
    print(f"🤖 AI Model: Gemini 2.5 Flash")
    print(f"💾 Database: {DATABASE}")
    print(f"📚 FAQ Source: {FAQ_FILE}")
    print("=" * 60)
    print("💡 Press CTRL+C to stop the server")
    print("=" * 60)
    
    # Start Flask development server
    app.run(debug=True, host='0.0.0.0', port=5000)
