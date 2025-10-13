@echo off
echo ===============================================
echo   AI Customer Support Bot - Frontend Setup
echo ===============================================
echo.

cd frontend

echo Installing dependencies...
call npm install

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo ERROR: Failed to install dependencies
    echo Make sure Node.js and npm are installed
    pause
    exit /b 1
)

echo.
echo ===============================================
echo   Setup Complete!
echo ===============================================
echo.
echo To start the frontend:
echo   1. cd frontend
echo   2. npm start
echo.
echo Make sure the Flask backend is running on port 5000
echo.
pause
