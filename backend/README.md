# AI Customer Support Bot - Backend

Flask-based backend API for the AI Customer Support chatbot powered by Google Gemini AI.

## 📁 Folder Structure

```
backend/
├── app/                    # Main application code
│   ├── __init__.py        # App package initialization
│   └── main.py            # Flask app and API endpoints
├── config/                # Configuration files
│   └── faqs.txt           # FAQ knowledge base
├── data/                  # Data storage
│   └── conversations.db   # SQLite database
├── scripts/               # Utility scripts
│   ├── demo.py            # Demo script
│   ├── diagnose.py        # Diagnostic tool
│   └── list_models.py     # List available Gemini models
├── tests/                 # Test files
│   ├── test_api.py        # API endpoint tests
│   └── quick_test.py      # Quick functionality test
├── __init__.py            # Backend package initialization
├── .env.example           # Example environment variables
├── requirements.txt       # Python dependencies
└── run.py                 # Server startup script
```

## 🚀 Quick Start

### 1. Install Dependencies

```bash
cd backend
pip install -r requirements.txt
```

### 2. Configure Environment

Create a `.env` file in the backend directory:

```bash
cp .env.example .env
```

Edit `.env` and add your Gemini API key:

```
GEMINI_API_KEY=your_api_key_here
```

### 3. Run the Server

```bash
python run.py
```

The server will start at `http://localhost:5000`

## 📡 API Endpoints

### Health Check
```http
GET /health
```

### Send Chat Message
```http
POST /chat
Content-Type: application/json

{
  "session_id": "user123",
  "message": "What is your return policy?"
}
```

### Request Escalation
```http
POST /escalate
Content-Type: application/json

{
  "session_id": "user123"
}
```

## 🧪 Running Tests

```bash
# Run all tests
cd tests
python test_api.py

# Quick functionality test
python quick_test.py
```

## 🛠️ Utility Scripts

```bash
# List available Gemini models
python scripts/list_models.py

# Run diagnostic checks
python scripts/diagnose.py

# Run demo conversation
python scripts/demo.py
```

## 🔧 Configuration

### FAQ Knowledge Base
Edit `config/faqs.txt` to update the chatbot's knowledge base.

### Model Parameters
Edit `app/main.py` to adjust Gemini model settings:
- `temperature`: Response creativity (0.0-1.0)
- `max_output_tokens`: Maximum response length
- `top_p`, `top_k`: Token selection parameters

## 📦 Dependencies

- Flask 3.0.0 - Web framework
- Flask-CORS - CORS support
- google-generativeai - Gemini AI SDK
- python-dotenv - Environment variable management

## 🔐 Security Notes

- Never commit `.env` file with real API keys
- Keep `GEMINI_API_KEY` secret
- Enable authentication for production deployment
- Use HTTPS in production

## 📝 License

MIT License - See project root for details
