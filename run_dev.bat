@echo off
SETLOCAL

REM Check if Python virtual environment is activated
IF "%VIRTUAL_ENV%"=="" (
    echo Python virtual environment is not activated.
    echo Please activate your virtual environment first.
    echo Example: venv\Scripts\activate
    exit /b 1
)

REM Start Django backend server
echo Starting Django backend server...
start cmd /k "python manage.py runserver"

REM Wait a moment for the backend to start
timeout /t 3 /nobreak > nul

REM Start SvelteKit frontend server
echo Starting SvelteKit frontend server...
cd frontend && start cmd /k "npm run dev -- --open"

echo.
echo Django backend running at http://localhost:8000/
echo SvelteKit frontend running at http://localhost:5173/
echo.
echo Close the command windows to stop the servers.

ENDLOCAL 