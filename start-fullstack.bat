@echo off
echo ===============================================
echo   AI Customer Support Bot - Full Stack Startup
echo ===============================================
echo.

echo Starting Flask Backend...
start "Flask Backend" cmd /k "venv\Scripts\activate && python app.py"

timeout /t 5 /nobreak >nul

echo Starting React Frontend...
cd frontend
start "React Frontend" cmd /k "npm start"

echo.
echo ===============================================
echo   Both servers are starting...
echo ===============================================
echo.
echo Backend: http://localhost:5000
echo Frontend: http://localhost:3000
echo.
echo Press any key to exit this window...
pause >nul
