# AI Customer Support Bot — Detailed Step-by-Step Implementation Plan

**Based on Product Documentation v3 (Flask + SQLite + Gemini API)**

This is a **click-by-click, error-minimizing implementation guide** for building the AI Customer Support Bot. It is designed for AI agents and developers to follow sequentially with minimal ambiguity. Each step includes commands, code snippets, and validation checks.

---

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Phase 1: Project Initialization](#phase-1-project-initialization)
3. [Phase 2: Database Setup](#phase-2-database-setup)
4. [Phase 3: FAQ Document Preparation](#phase-3-faq-document-preparation)
5. [Phase 4: Gemini API Integration](#phase-4-gemini-api-integration)
6. [Phase 5: Flask API Endpoint Development](#phase-5-flask-api-endpoint-development)
7. [Phase 6: Conversation Logic Implementation](#phase-6-conversation-logic-implementation)
8. [Phase 7: Escalation Workflow](#phase-7-escalation-workflow)
9. [Phase 8: Testing](#phase-8-testing)
10. [Phase 9: Documentation](#phase-9-documentation)
11. [Phase 10: Demo Video](#phase-10-demo-video)
12. [Phase 11: Final Delivery](#phase-11-final-delivery)

---

## Prerequisites

- **Python 3.8+** installed
- **Git** installed
- **GitHub account** (username: Aviral-Dwivedi-0)
- **Gemini API key** (from Google AI Studio)
- **Text editor or IDE** (VS Code, PyCharm, etc.)
- **Postman** or **curl** for API testing

---

## Phase 1: Project Initialization

### Step 1.1: Create GitHub Repository

1. Go to [https://github.com](https://github.com)
2. Click **"New"** button (top right, green)
3. Fill in:
   - Repository name: `ai-customer-support-bot`
   - Description: `AI-powered customer support bot using Flask, SQLite, and Gemini API`
   - Visibility: **Public**
   - Check **"Add a README file"**
   - Add `.gitignore`: Select **Python**
   - License: **MIT License**
4. Click **"Create repository"**

### Step 1.2: Clone Repository Locally

Open terminal and run:

```bash
git clone https://github.com/Aviral-Dwivedi-0/ai-customer-support-bot.git
cd ai-customer-support-bot
```

### Step 1.3: Set Up Python Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install --upgrade pip
```

### Step 1.4: Create Project Files

```bash
touch app.py
touch faqs.txt
touch requirements.txt
touch .env
```

### Step 1.5: Add Dependencies to requirements.txt

Open `requirements.txt` and add:

```
flask==3.0.0
google-generativeai==0.3.1
python-dotenv==1.0.0
```

### Step 1.6: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 1.7: Initial Commit

```bash
git add .
git commit -m "Initial project setup with dependencies"
git push origin main
```

**✅ Validation:** Check GitHub repository shows the committed files.

---

## Phase 2: Database Setup

### Step 2.1: Create Database Initialization Code

Open `app.py` and add:

```python
import sqlite3
import os

DATABASE = 'conversations.db'

def init_db():
    """Initialize the SQLite database"""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS conversations (
            session_id TEXT PRIMARY KEY,
            history TEXT
        )
    ''')
    conn.commit()
    conn.close()
    print("Database initialized successfully")

if __name__ == '__main__':
    init_db()
```

### Step 2.2: Test Database Creation

```bash
python app.py
```

**✅ Validation:** Check that `conversations.db` file is created in the project directory.

### Step 2.3: Add Database Helper Functions

Add these functions to `app.py`:

```python
def get_session_history(session_id):
    """Retrieve conversation history for a session"""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT history FROM conversations WHERE session_id = ?', (session_id,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else ""

def save_session_history(session_id, history):
    """Save or update conversation history for a session"""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT OR REPLACE INTO conversations (session_id, history)
        VALUES (?, ?)
    ''', (session_id, history))
    conn.commit()
    conn.close()
```

### Step 2.4: Commit Database Code

```bash
git add app.py conversations.db
git commit -m "Add SQLite database setup and helper functions"
git push origin main
```

---

## Phase 3: FAQ Document Preparation

### Step 3.1: Create FAQ Content

Open `faqs.txt` and add sample FAQs:

```
Q: What is your return policy?
A: You can return products within 30 days of purchase with original packaging and receipt.

Q: Do you ship internationally?
A: Yes, we ship to over 50 countries worldwide. Shipping costs vary by location.

Q: What payment methods do you accept?
A: We accept credit cards (Visa, MasterCard, American Express), PayPal, and bank transfers.

Q: How long does shipping take?
A: Domestic shipping takes 3-5 business days. International shipping takes 7-14 business days.

Q: Do you offer warranty on products?
A: Yes, all products come with a 1-year manufacturer's warranty.

Q: How can I track my order?
A: Once your order ships, you will receive a tracking number via email.

Q: What is your customer service phone number?
A: You can reach us at 1-800-SUPPORT (1-800-787-7678) from 9 AM to 6 PM EST.

Q: Can I modify my order after placing it?
A: Orders can be modified within 1 hour of placement. Contact customer service immediately.
```

### Step 3.2: Create FAQ Loader Function

Add to `app.py`:

```python
def load_faqs():
    """Load FAQ content from file"""
    if not os.path.exists('faqs.txt'):
        print("ERROR: faqs.txt not found")
        return ""

    with open('faqs.txt', 'r', encoding='utf-8') as f:
        faqs_content = f.read()

    print(f"Loaded {len(faqs_content)} characters from FAQs")
    return faqs_content

# Global variable to store FAQs
FAQ_CONTENT = load_faqs()
```

### Step 3.3: Commit FAQ Files

```bash
git add faqs.txt app.py
git commit -m "Add FAQ document and loader function"
git push origin main
```

---

## Phase 4: Gemini API Integration

### Step 4.1: Get Gemini API Key

1. Go to [https://makersuite.google.com/app/apikey](https://makersuite.google.com/app/apikey)
2. Click **"Create API Key"**
3. Copy the API key

### Step 4.2: Store API Key Securely

Open `.env` file and add:

```
GEMINI_API_KEY=your_actual_api_key_here
```

**⚠️ Important:** Add `.env` to `.gitignore` to avoid committing secrets:

```bash
echo ".env" >> .gitignore
```

### Step 4.3: Create Gemini Service Module

Add to `app.py`:

```python
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini API
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found in environment variables")

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-pro')

def call_gemini(prompt):
    """Call Gemini API with the given prompt"""
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        print(f"Error calling Gemini API: {e}")
        return "ESCALATE"
```

### Step 4.4: Test Gemini Integration

Add a test block to `app.py`:

```python
def test_gemini():
    """Test Gemini API connection"""
    test_prompt = "Say 'Hello, I am working!' if you can read this."
    response = call_gemini(test_prompt)
    print(f"Gemini Test Response: {response}")

# Uncomment to test:
# test_gemini()
```

Run:

```bash
python app.py
```

**✅ Validation:** Uncomment `test_gemini()`, run, and verify you get a response.

### Step 4.5: Commit Gemini Integration

```bash
git add app.py .gitignore
git commit -m "Add Gemini API integration with secure key storage"
git push origin main
```

---

## Phase 5: Flask API Endpoint Development

### Step 5.1: Set Up Flask App

Replace the main block in `app.py` with:

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    """Main chat endpoint"""
    try:
        data = request.get_json()

        # Validate input
        if not data or 'session_id' not in data or 'query' not in data:
            return jsonify({"error": "Missing session_id or query"}), 400

        session_id = data['session_id']
        user_query = data['query']

        # Placeholder response
        return jsonify({"response": "Bot is under construction"})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({"status": "ok"}), 200

if __name__ == '__main__':
    init_db()
    app.run(debug=True, host='0.0.0.0', port=5000)
```

### Step 5.2: Test Flask Server

```bash
python app.py
```

**✅ Validation:** Open browser to `http://localhost:5000/health` — should return `{"status": "ok"}`

### Step 5.3: Test Chat Endpoint with curl

Open a new terminal:

```bash
curl -X POST http://localhost:5000/chat \
  -H "Content-Type: application/json" \
  -d '{"session_id": "test123", "query": "Hello"}'
```

**✅ Validation:** Should return `{"response": "Bot is under construction"}`

### Step 5.4: Commit Flask Setup

```bash
git add app.py
git commit -m "Add Flask API with /chat and /health endpoints"
git push origin main
```

---

## Phase 6: Conversation Logic Implementation

### Step 6.1: Create Prompt Constructor

Add to `app.py`:

```python
def construct_prompt(user_query, history, faqs):
    """Construct the full prompt for Gemini"""
    prompt = f"""You are a customer support bot. Answer the user's query based ONLY on the provided FAQs. If the answer isn't in the FAQs, respond with the exact phrase 'ESCALATE'.

FAQs:
{faqs}

Conversation History:
{history}

New User Query:
{user_query}

Your Response:"""

    return prompt
```

### Step 6.2: Implement Full Chat Logic

Update the `/chat` endpoint in `app.py`:

```python
@app.route('/chat', methods=['POST'])
def chat():
    """Main chat endpoint"""
    try:
        data = request.get_json()

        # Validate input
        if not data or 'session_id' not in data or 'query' not in data:
            return jsonify({"error": "Missing session_id or query"}), 400

        session_id = data['session_id']
        user_query = data['query']

        # Step 1: Retrieve conversation history
        history = get_session_history(session_id)

        # Step 2: Construct full prompt
        full_prompt = construct_prompt(user_query, history, FAQ_CONTENT)

        # Step 3: Call Gemini API
        bot_response = call_gemini(full_prompt)

        # Step 4: Check for escalation
        if bot_response == "ESCALATE":
            bot_response = "I can't answer that question. I will escalate this to a human agent."

        # Step 5: Update history
        new_history = history + f"\nUser: {user_query}\nBot: {bot_response}"
        save_session_history(session_id, new_history)

        # Step 6: Return response
        return jsonify({"response": bot_response})

    except Exception as e:
        print(f"Error in /chat endpoint: {e}")
        return jsonify({"error": "Internal server error"}), 500
```

### Step 6.3: Test Full Workflow

Restart Flask server and test:

```bash
# Test 1: FAQ match
curl -X POST http://localhost:5000/chat \
  -H "Content-Type: application/json" \
  -d '{"session_id": "session1", "query": "What is your return policy?"}'

# Test 2: Follow-up (tests history)
curl -X POST http://localhost:5000/chat \
  -H "Content-Type: application/json" \
  -d '{"session_id": "session1", "query": "How many days?"}'

# Test 3: Escalation
curl -X POST http://localhost:5000/chat \
  -H "Content-Type: application/json" \
  -d '{"session_id": "session2", "query": "What is the meaning of life?"}'
```

**✅ Validation:**

- Test 1 should return the return policy
- Test 2 should understand context and respond about 30 days
- Test 3 should return escalation message

### Step 6.4: Commit Conversation Logic

```bash
git add app.py
git commit -m "Implement full conversation logic with history and context"
git push origin main
```

---

## Phase 7: Escalation Workflow

### Step 7.1: Add Conversation Summarization

Add to `app.py`:

```python
def summarize_conversation(history):
    """Use Gemini to summarize conversation for agent handoff"""
    if not history.strip():
        return "No conversation history available."

    summary_prompt = f"""Summarize the following customer support conversation concisely for a human agent:

{history}

Summary:"""

    try:
        summary = call_gemini(summary_prompt)
        return summary
    except Exception as e:
        return f"Error generating summary: {e}"
```

### Step 7.2: Enhance Escalation with Summary

Update the escalation logic in the `/chat` endpoint:

```python
        # Step 4: Check for escalation (ENHANCED)
        if bot_response == "ESCALATE":
            summary = summarize_conversation(history)
            bot_response = f"I can't answer that question. I will escalate this to a human agent.\n\nSummary for agent:\n{summary}"
```

### Step 7.3: Add Escalation Endpoint (Optional)

Add a dedicated endpoint for escalation details:

```python
@app.route('/escalate', methods=['POST'])
def escalate():
    """Get escalation summary for a session"""
    try:
        data = request.get_json()
        if not data or 'session_id' not in data:
            return jsonify({"error": "Missing session_id"}), 400

        session_id = data['session_id']
        history = get_session_history(session_id)
        summary = summarize_conversation(history)

        return jsonify({"summary": summary})

    except Exception as e:
        return jsonify({"error": str(e)}), 500
```

### Step 7.4: Test Escalation

```bash
# Trigger escalation
curl -X POST http://localhost:5000/chat \
  -H "Content-Type: application/json" \
  -d '{"session_id": "escalation_test", "query": "Can you help me with quantum physics?"}'

# Get escalation summary
curl -X POST http://localhost:5000/escalate \
  -H "Content-Type: application/json" \
  -d '{"session_id": "escalation_test"}'
```

**✅ Validation:** Should return escalation message with summary

### Step 7.5: Commit Escalation Features

```bash
git add app.py
git commit -m "Add escalation workflow with conversation summarization"
git push origin main
```

---

## Phase 8: Testing

### Step 8.1: Create Test Script

Create `test_api.py`:

```python
import requests
import json

BASE_URL = "http://localhost:5000"

def test_health():
    """Test health endpoint"""
    response = requests.get(f"{BASE_URL}/health")
    print(f"Health Check: {response.json()}")
    assert response.status_code == 200

def test_faq_match():
    """Test FAQ matching"""
    payload = {
        "session_id": "test_faq",
        "query": "Do you ship internationally?"
    }
    response = requests.post(f"{BASE_URL}/chat", json=payload)
    print(f"FAQ Test: {response.json()}")
    assert response.status_code == 200

def test_context_memory():
    """Test conversational context"""
    session_id = "test_context"

    # First query
    payload1 = {"session_id": session_id, "query": "What is your return policy?"}
    response1 = requests.post(f"{BASE_URL}/chat", json=payload1)
    print(f"Context Test 1: {response1.json()}")

    # Follow-up query
    payload2 = {"session_id": session_id, "query": "How many days do I have?"}
    response2 = requests.post(f"{BASE_URL}/chat", json=payload2)
    print(f"Context Test 2: {response2.json()}")

    assert "30" in response2.json()['response'] or "thirty" in response2.json()['response'].lower()

def test_escalation():
    """Test escalation trigger"""
    payload = {
        "session_id": "test_escalation",
        "query": "What is the weather today?"
    }
    response = requests.post(f"{BASE_URL}/chat", json=payload)
    print(f"Escalation Test: {response.json()}")
    assert "escalate" in response.json()['response'].lower()

if __name__ == "__main__":
    print("Running API Tests...\n")
    test_health()
    test_faq_match()
    test_context_memory()
    test_escalation()
    print("\n✅ All tests passed!")
```

### Step 8.2: Run Tests

With Flask server running:

```bash
python test_api.py
```

**✅ Validation:** All tests should pass

### Step 8.3: Commit Test Script

```bash
git add test_api.py
git commit -m "Add comprehensive API test script"
git push origin main
```

---

## Phase 9: Documentation

### Step 9.1: Create Comprehensive README

Create `README.md`:

````markdown
# AI Customer Support Bot

An AI-powered customer support chatbot built with Flask, SQLite, and Google's Gemini API. The bot answers queries based on a predefined FAQ document and escalates to human agents when necessary.

## Features

- ✅ FAQ-based question answering
- ✅ Conversational context memory
- ✅ Smart escalation to human agents
- ✅ Conversation summarization
- ✅ Simple REST API
- ✅ SQLite session management

## Tech Stack

- **Backend:** Flask (Python)
- **Database:** SQLite
- **LLM:** Google Gemini Pro API
- **Language:** Python 3.8+

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Aviral-Dwivedi-0/ai-customer-support-bot.git
cd ai-customer-support-bot
```

### 2. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Gemini API Key

Create a `.env` file:

```
GEMINI_API_KEY=your_gemini_api_key_here
```

Get your API key from [Google AI Studio](https://makersuite.google.com/app/apikey).

### 5. Run the Application

```bash
python app.py
```

The server will start on `http://localhost:5000`

## API Documentation

### POST /chat

Send a message to the chatbot.

**Request:**

```json
{
  "session_id": "unique_session_id",
  "query": "What is your return policy?"
}
```

**Response:**

```json
{
  "response": "You can return products within 30 days of purchase..."
}
```

### GET /health

Health check endpoint.

**Response:**

```json
{
  "status": "ok"
}
```

### POST /escalate

Get conversation summary for agent handoff.

**Request:**

```json
{
  "session_id": "unique_session_id"
}
```

**Response:**

```json
{
  "summary": "Customer asked about return policy and shipping times..."
}
```

## Prompt Engineering

### Main Prompt Structure

```
System Instruction:
You are a customer support bot. Answer based ONLY on provided FAQs.
If answer not in FAQs, respond with 'ESCALATE'.

FAQs:
[Full FAQ content]

Conversation History:
[Previous messages]

New User Query:
[Current question]
```

### Escalation Trigger

When Gemini responds with exactly "ESCALATE", the bot:

1. Generates a conversation summary
2. Returns escalation message with summary

## Testing

Run the test suite:

```bash
python test_api.py
```

Tests cover:

- Health check
- FAQ matching
- Context memory
- Escalation workflow

## Project Structure

```
├── app.py                 # Main Flask application
├── faqs.txt              # FAQ knowledge base
├── conversations.db      # SQLite database (auto-created)
├── requirements.txt      # Python dependencies
├── test_api.py          # API test suite
├── .env                 # Environment variables (not in git)
└── README.md            # This file
```

## Customization

### Adding FAQs

Edit `faqs.txt` with this format:

```
Q: Your question here?
A: Your answer here.
```

Restart the server to load new FAQs.

### Adjusting Context Window

Modify the history retrieval in `construct_prompt()` to limit context size.

## Demo

[Link to demo video]

## License

MIT License

## Author

Aviral Dwivedi (Aviral-Dwivedi-0)
````

Step 9.2: Commit README
bash
git add README.md
git commit -m "Add comprehensive README documentation"
git push origin main
Phase 10: Demo Video
Step 10.1: Prepare Demo Script
Demo should showcase:

Health Check — Show /health endpoint
FAQ Match — Ask "What is your return policy?"
Context Memory — Follow-up "How many days?"
Escalation — Ask unrelated question
Summary — Call /escalate endpoint
Step 10.2: Record Demo
Use one of these tools:

Postman: Record screen while making requests
curl + screen recording: Use OBS Studio or QuickTime
Loom (free): loom.com
Step 10.3: Upload Demo
Upload to YouTube (unlisted) or Loom
Add link to README under "Demo" section
Step 10.4: Commit Demo Link
bash
git add README.md
git commit -m "Add demo video link to README"
git push origin main
Phase 11: Final Delivery
Step 11.1: Final Code Review Checklist
All endpoints tested and working
Error handling in place
Code comments added for complex logic
No hardcoded secrets (API keys in .env)
.gitignore includes .env and pycache
README is complete and accurate
requirements.txt is up to date
Demo video is accessible
Step 11.2: Clean Up Code
Remove any test functions and debug print statements:

Python

# Remove or comment out:

# test_gemini()

Step 11.3: Final Commit
bash
git add .
git commit -m "Final cleanup and production-ready code"
git push origin main
Step 11.4: Create GitHub Release
Go to repository on GitHub
Click "Releases" → "Create a new release"
Tag: v1.0.0
Title: AI Customer Support Bot v1.0.0
Description: Summary of features
Click "Publish release"
Step 11.5: Verify Deliverables
✅ GitHub repository is public
✅ README.md is comprehensive
✅ Demo video is linked
✅ Code is clean and commented
✅ All features work as expected

Troubleshooting Guide
Common Issues
Issue: GEMINI_API_KEY not found
Solution: Ensure .env file exists and contains your API key

Issue: Database locked error
Solution: Close all connections; restart Flask server

Issue: Gemini API rate limit
Solution: Add retry logic or use free tier limits wisely

Issue: Escalation not triggering
Solution: Check if Gemini returns exactly "ESCALATE" (case-sensitive)

Next Steps / Enhancements
Add rate limiting to prevent abuse
Implement user authentication
Add logging for debugging
Deploy to cloud (Heroku, Railway, Render)
Add frontend chat UI
Implement caching for frequent queries
Add analytics _dashboard_
