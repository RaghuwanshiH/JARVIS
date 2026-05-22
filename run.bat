@echo off
echo Starting Phi-3 3.8B on RTX 3050...
echo Choose mode:
echo 1. Web UI
echo 2. CLI Terminal
set /p choice=Enter 1 or 2: 

start /b ollama serve
timeout /t 2 /nobreak >nul

if %choice%==1 python python/app.py
if %choice%==2 python python/test.py

pause
