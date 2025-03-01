#!/bin/bash

# Function to handle cleanup on exit
cleanup() {
    echo "Shutting down servers..."
    kill $BACKEND_PID $FRONTEND_PID 2>/dev/null
    exit 0
}

# Set up trap to catch SIGINT (Ctrl+C)
trap cleanup SIGINT

# Check if Python virtual environment is activated
if [ -z "$VIRTUAL_ENV" ]; then
    echo "Python virtual environment is not activated."
    echo "Please activate your virtual environment first."
    echo "Example: source venv/bin/activate"
    exit 1
fi

# Start Django backend server
echo "Starting Django backend server..."
python manage.py runserver &
BACKEND_PID=$!

# Check if backend started successfully
sleep 2
if ! ps -p $BACKEND_PID > /dev/null; then
    echo "Failed to start Django backend server."
    exit 1
fi

echo "Django backend running at http://localhost:8000/"

# Start SvelteKit frontend server
echo "Starting SvelteKit frontend server..."
cd frontend && npm run dev -- --open &
FRONTEND_PID=$!

# Check if frontend started successfully
sleep 5
if ! ps -p $FRONTEND_PID > /dev/null; then
    echo "Failed to start SvelteKit frontend server."
    kill $BACKEND_PID
    exit 1
fi

echo "SvelteKit frontend running at http://localhost:5173/"
echo "Press Ctrl+C to stop both servers."

# Wait for both processes
wait $BACKEND_PID $FRONTEND_PID 