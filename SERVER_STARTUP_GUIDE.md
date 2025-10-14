# 🚀 Quick Server Startup Guide

## Issue with PowerShell

**Problem:** In PowerShell, batch files must be prefixed with `.\`

❌ **Wrong:**

```powershell
start-fullstack.bat
```

✅ **Correct:**

```powershell
.\start-fullstack.bat
```

---

## Manual Startup (Recommended for Development)

### Option 1: Using Full Path (Most Reliable)

**Backend:**

```powershell
# From project root
python backend\run.py
```

**Frontend:** (New Terminal)

```powershell
# From project root
cd frontend
npm start
```

### Option 2: Using Batch Script

```powershell
.\start-fullstack.bat
```

---

## Current Server Status

✅ **Backend:** Running at http://localhost:5000
✅ **Frontend:** Running at http://localhost:3000

---

## Troubleshooting

### Backend Not Starting?

**Check 1: Virtual Environment**

```powershell
.\venv\Scripts\activate
```

**Check 2: Dependencies**

```powershell
cd backend
pip install -r requirements.txt
```

**Check 3: Environment Variables**

```powershell
# Make sure .env file exists in backend/
# Should contain: GEMINI_API_KEY=your_key_here
```

### Frontend Not Starting?

**Check 1: Node Modules**

```powershell
cd frontend
npm install
```

**Check 2: Port 3000 In Use**

```powershell
# Kill process on port 3000
netstat -ano | findstr :3000
# Then kill the PID shown
taskkill /PID <PID> /F
```

---

## Testing Your Setup

### Quick Test - Backend Health Check

```powershell
curl http://localhost:5000/health
```

Expected Response:

```json
{ "status": "ok" }
```

### Quick Test - Send a Message

```powershell
curl -X POST http://localhost:5000/chat `
  -H "Content-Type: application/json" `
  -d '{\"session_id\": \"test123\", \"query\": \"What is your return policy?\"}'
```

### Open in Browser

- **Frontend:** http://localhost:3000
- **Backend API:** http://localhost:5000/health

---

## Useful Commands

### Stop Servers

```powershell
# Press Ctrl+C in each terminal window
```

### Check What's Running

```powershell
# Check backend (port 5000)
netstat -ano | findstr :5000

# Check frontend (port 3000)
netstat -ano | findstr :3000
```

### View Logs

Backend logs appear in the terminal where you ran `python backend\run.py`
Frontend logs appear in the terminal where you ran `npm start`

---

## Summary

**✅ WORKING SETUP:**

1. Terminal 1: `python backend\run.py` (from project root)
2. Terminal 2: `cd frontend && npm start`
3. Browser: Open http://localhost:3000

**Your application is now running successfully!** 🎉
