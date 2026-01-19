@echo off
echo ========================================
echo VAPA Order System - Local Server
echo ========================================
echo.
echo Installing required packages...
pip install -r requirements.txt
echo.
echo Starting server...
echo.
echo Your application will be available at:
echo http://localhost:5000
echo.
echo Press Ctrl+C to stop the server
echo.
python app.py
pause
