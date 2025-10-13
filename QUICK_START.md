# 🎯 Quick Start Guide - AI Customer Support Bot

## ⚡ 5-Minute Setup

### 1. Navigate to Project
```bash
cd "d:\Unthinkable Assignment"
```

### 2. Activate Virtual Environment
```bash
venv\Scripts\activate
```

### 3. Start the Server
```bash
python app.py
```

✅ Server runs on: http://localhost:5000

---

## 🧪 Testing

### Quick Test (2 scenarios)
```bash
python quick_test.py
```

### Full Test Suite (5 tests)
```bash
python test_api.py
```

### Live Demonstration (5 scenarios)
```bash
python demo.py
```

---

## 📡 API Usage Examples

### Using curl (Windows PowerShell)

#### Health Check
```powershell
curl http://localhost:5000/health
```

#### Ask a Question
```powershell
curl -X POST http://localhost:5000/chat `
  -H "Content-Type: application/json" `
  -d '{\"session_id\": \"user123\", \"query\": \"What is your return policy?\"}'
```

#### Get Conversation Summary
```powershell
curl -X POST http://localhost:5000/escalate `
  -H "Content-Type: application/json" `
  -d '{\"session_id\": \"user123\"}'
```

### Using Python

```python
import requests

# Ask a question
response = requests.post('http://localhost:5000/chat', json={
    'session_id': 'user123',
    'query': 'Do you ship internationally?'
})

print(response.json()['response'])
```

---

## 📁 Important Files

| File | Purpose |
|------|---------|
| `app.py` | Main Flask application |
| `faqs.txt` | FAQ knowledge base |
| `.env` | API keys (DO NOT commit to git) |
| `test_api.py` | Comprehensive test suite |
| `demo.py` | Live demonstration script |
| `README.md` | Full documentation |
| `PROJECT_SUMMARY.md` | Completion report |

---

## 🔧 Troubleshooting

### Server won't start?
```bash
# Make sure virtual environment is activated
venv\Scripts\activate

# Check if Python is available
python --version

# Try restarting
python app.py
```

### Tests failing?
```bash
# Make sure server is running in another terminal
# Then run tests
python test_api.py
```

### API not responding?
```bash
# Check if server is running
# Visit: http://localhost:5000/health
```

---

## 🎓 What Does It Do?

✅ **Answers FAQ questions** using AI  
✅ **Remembers conversation** context  
✅ **Escalates unknown** questions to humans  
✅ **Summarizes conversations** for agents  
✅ **Stores sessions** in SQLite database  

---

## 📊 Test Results

All 5 tests **PASSED** ✅

1. ✅ Health check
2. ✅ FAQ matching
3. ✅ Context memory
4. ✅ Escalation
5. ✅ Summary generation

---

## 🚀 Next Steps

### To customize FAQs:
Edit `faqs.txt` and restart server

### To deploy:
See `README.md` for deployment options

### To add features:
Check `PROJECT_SUMMARY.md` for enhancement ideas

---

## 📞 Support

For issues or questions, refer to:
- `README.md` - Complete documentation
- `PROJECT_SUMMARY.md` - Technical details
- `Implementation_Plan.md` - Original plan

---

**Built with Flask, SQLite, and Google Gemini AI** 🤖
