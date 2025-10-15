# AI Customer Support Bot

An AI-powered customer support chatbot with a beautiful React frontend and Flask backend, powered by Google's Gemini API.

## 🌐 Live Demo

**🚀 Try it now:** [https://ai-customer-support-bot-frontend.vercel.app](https://ai-customer-support-bot-frontend.vercel.app)

**Deployment Links:**
- **Frontend (React):** [https://ai-customer-support-bot-frontend.vercel.app](https://ai-customer-support-bot-frontend.vercel.app)
- **Backend API (Flask):** [https://ai-customer-support-bot-beta.vercel.app](https://ai-customer-support-bot-beta.vercel.app)

---

## ✨ Features

- ✅ **Beautiful React Frontend** - Modern, responsive chat interface
- ✅ **FAQ-based Answering** - Intelligent responses from knowledge base
- ✅ **Context Memory** - Remembers conversation history
- ✅ **Smart Escalation** - Routes complex queries to human agents
- ✅ **Conversation Summaries** - For seamless agent handoff
- ✅ **REST API** - Clean backend architecture
- ✅ **SQLite Storage** - Persistent session management
- ✅ **Real-time Chat** - Instant messaging with typing indicators

## 🛠 Tech Stack

**Frontend:**

- ⚛️ React 18
- 📡 Axios
- 🎨 Custom CSS with animations
- 📱 Responsive design

**Backend:**

- 🐍 Flask (Python)
- 🗄️ SQLite
- 🤖 Google Gemini 2.5 Flash AI
- 🔐 Flask-CORS

## 🚀 Quick Start

### Full Stack (Automated - Windows)

```bash
# Run both frontend and backend
start-fullstack.bat
```

Access the app at:

- **Frontend:** http://localhost:3000
- **Backend API:** http://localhost:5000

### Backend Only

```bash
# Activate virtual environment
venv\Scripts\activate

# Navigate to backend
cd backend

# Start Flask server
python run.py
```

### Frontend Only

```bash
# Navigate to frontend
cd frontend

# Install dependencies (first time)
npm install

# Start development server
npm start
```

## 📋 Detailed Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Aviral-Dwivedi-0/ai-customer-support-bot.git
cd ai-customer-support-bot
```

### 2. Create Virtual Environment

```bash
python -m venv venv

# On Windows:
venv\Scripts\activate

# On Mac/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

**Backend:**

```bash
cd backend
pip install -r requirements.txt
```

**Frontend:**

```bash
cd frontend
npm install
```

### 4. Configure Gemini API Key

1. Get your API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a `.env` file in the **backend** directory:

```bash
cd backend
cp .env.example .env
```

3. Edit `.env` and add your API key:

```
GEMINI_API_KEY=your_actual_gemini_api_key_here
```

**⚠️ Important:** Never commit your `.env` file to version control!

### 5. Run the Application

```bash
python app.py
```

The server will start on `http://localhost:5000`

## API Documentation

### GET /health

Health check endpoint to verify the server is running.

**Response:**

```json
{
  "status": "ok"
}
```

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
  "response": "You can return products within 30 days of purchase with original packaging and receipt."
}
```

**Escalation Response:**

```json
{
  "response": "I can't answer that question. I will escalate this to a human agent.\n\nSummary for agent:\n[Conversation summary]"
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

## Testing

Run the comprehensive test suite:

```bash
python test_api.py
```

Tests cover:

- ✅ Health check
- ✅ FAQ matching
- ✅ Context memory (follow-up questions)
- ✅ Escalation workflow
- ✅ Summary generation

## How It Works

### 1. In-Context Learning Approach

Instead of using vector databases or RAG, this bot uses **in-context learning**:

- Every query sends the complete FAQ document to Gemini
- Conversation history is included for context
- The LLM responds based only on the provided FAQs

### 2. Prompt Structure

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

### 3. Escalation Logic

When Gemini responds with exactly `"ESCALATE"`, the bot:

1. Detects the escalation trigger
2. Generates a conversation summary using Gemini
3. Returns escalation message with summary for human agent

### 4. Session Management

- Each conversation has a unique `session_id`
- All messages are stored in SQLite
- History is retrieved and updated with each interaction

## Project Structure

```
├── app.py                 # Main Flask application
├── faqs.txt              # FAQ knowledge base
├── conversations.db      # SQLite database (auto-created)
├── requirements.txt      # Python dependencies
├── test_api.py          # API test suite
├── .env                 # Environment variables (not in git)
├── .env.example         # Environment template
├── .gitignore           # Git ignore rules
└── README.md            # This file
```

## Customization

### Adding FAQs

Edit `faqs.txt` with this format:

```
Q: Your question here?
A: Your answer here.

Q: Another question?
A: Another answer.
```

Restart the server to load new FAQs.

### Adjusting the Model

Change the model in `app.py`:

```python
model = genai.GenerativeModel('gemini-pro')  # or 'gemini-1.5-pro'
```

### Limiting Context Window

Modify `construct_prompt()` to truncate history if it gets too long.

## Example Usage

### Using curl

```bash
# Test health
curl http://localhost:5000/health

# Ask a question
curl -X POST http://localhost:5000/chat \
  -H "Content-Type: application/json" \
  -d '{"session_id": "user123", "query": "Do you ship internationally?"}'

# Follow-up question
curl -X POST http://localhost:5000/chat \
  -H "Content-Type: application/json" \
  -d '{"session_id": "user123", "query": "How long does it take?"}'

# Get conversation summary
curl -X POST http://localhost:5000/escalate \
  -H "Content-Type: application/json" \
  -d '{"session_id": "user123"}'
```

### Using Python

```python
import requests

response = requests.post('http://localhost:5000/chat', json={
    'session_id': 'user123',
    'query': 'What is your return policy?'
})

print(response.json()['response'])
```

## Troubleshooting

### Issue: `GEMINI_API_KEY not found`

**Solution:** Make sure you created a `.env` file with your API key.

### Issue: `Database locked error`

**Solution:** Close all connections and restart the Flask server.

### Issue: Gemini API rate limit

**Solution:** The free tier has rate limits. Wait a few minutes or upgrade your API plan.

### Issue: Escalation not triggering

**Solution:** Check if Gemini returns exactly `"ESCALATE"` (case-sensitive). Adjust the prompt if needed.

## Future Enhancements

- [ ] Add rate limiting to prevent abuse
- [ ] Implement user authentication
- [ ] Add comprehensive logging
- [ ] Deploy to cloud (Heroku, Railway, Render)
- [ ] Create frontend chat UI
- [ ] Implement caching for frequent queries
- [ ] Add analytics dashboard
- [ ] Support multiple languages

## License

MIT License

## Author

Aviral Dwivedi ([@Aviral-Dwivedi-0](https://github.com/Aviral-Dwivedi-0))

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
