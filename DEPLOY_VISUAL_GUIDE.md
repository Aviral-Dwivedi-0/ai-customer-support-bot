# 🚀 Vercel Deployment - Quick Visual Guide

## ✅ All Code Committed!

Your code is ready on GitHub: 
`https://github.com/Aviral-Dwivedi-0/ai-customer-support-bot`

---

## 📋 6-Step Deployment Process

### STEP 1️⃣: Sign Up for Vercel
```
1. Go to: https://vercel.com
2. Click "Sign Up"
3. Choose "Continue with GitHub"
4. Authorize Vercel
```
⏱️ Time: 2 minutes

---

### STEP 2️⃣: Deploy Backend
```
1. Vercel Dashboard → "Add New" → "Project"
2. Import: ai-customer-support-bot
3. Configure:
   - Project Name: ai-support-backend
   - Framework: Other
   - Root Directory: backend ⚠️ IMPORTANT!
4. Environment Variables:
   - GEMINI_API_KEY = [your-api-key]
5. Click "Deploy"
6. 📋 SAVE THE BACKEND URL!
```
⏱️ Time: 5 minutes  
📋 Save: `https://ai-support-backend.vercel.app`

---

### STEP 3️⃣: Update Frontend Code
```
1. Open: frontend/src/App.js
2. Find line 12:
   const API_URL = 'http://localhost:5000';
3. Replace with:
   const API_URL = process.env.REACT_APP_API_URL || 'YOUR_BACKEND_URL';
4. Save file
5. Git commit & push:
   git add frontend/src/App.js
   git commit -m "Update API URL for Vercel"
   git push origin main
```
⏱️ Time: 3 minutes

---

### STEP 4️⃣: Deploy Frontend
```
1. Vercel Dashboard → "Add New" → "Project"
2. Import: ai-customer-support-bot (SAME repo)
3. Configure:
   - Project Name: ai-support-frontend
   - Framework: Create React App
   - Root Directory: frontend ⚠️ IMPORTANT!
4. Environment Variables:
   - REACT_APP_API_URL = [your-backend-url]
5. Click "Deploy"
6. 📋 SAVE THE FRONTEND URL!
```
⏱️ Time: 5 minutes  
📋 Save: `https://ai-support-frontend.vercel.app`

---

### STEP 5️⃣: Update CORS
```
1. Open: backend/app/main.py
2. Find CORS configuration (line ~40-50)
3. Add your frontend URL to origins:
   "origins": [
       "http://localhost:3000",
       "https://ai-support-frontend.vercel.app",  ← Add
       "https://*.vercel.app"  ← Add
   ]
4. Save file
5. Git commit & push:
   git add backend/app/main.py
   git commit -m "Update CORS for Vercel"
   git push origin main
```
⏱️ Time: 3 minutes  
✅ Backend auto-redeploys

---

### STEP 6️⃣: Test Your App
```
1. Open: https://your-frontend.vercel.app
2. Try asking:
   - "What payment methods do you accept?"
   - "How do I return a product?"
   - "Do you offer free shipping?"
3. If working → 🎉 SUCCESS!
```
⏱️ Time: 2 minutes

---

## 🎯 Total Time: ~20 minutes

---

## 🆘 Quick Troubleshooting

| Problem | Solution |
|---------|----------|
| Network Error | Check REACT_APP_API_URL env variable |
| CORS Error | Update CORS in backend/app/main.py |
| 500 Error | Check GEMINI_API_KEY is set correctly |
| Build Failed | Check Vercel build logs |

---

## 📊 What You'll Get

After deployment:

**Backend API:**  
`https://ai-support-backend.vercel.app`

**Frontend Website:**  
`https://ai-support-frontend.vercel.app`

**Features:**
- ✅ 150+ FAQ questions
- ✅ AI-powered chat
- ✅ Professional e-commerce bot
- ✅ Live on the internet!

---

## 📚 Detailed Instructions

For complete step-by-step guide, see:  
**`VERCEL_STEP_BY_STEP.txt`**

---

## 🎉 Ready to Deploy!

Start with STEP 1 above and follow through to STEP 6.

**Good luck! 🚀**
