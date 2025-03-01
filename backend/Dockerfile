# For production:
# - Consider using a multi-stage build for smaller images
# - Add proper health checks
# - Consider using gunicorn/uvicorn instead of Django's development server
# - Implement proper static file handling

FROM python:3.10-slim

WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# PROD: For production, you might want to add:
# RUN pip install gunicorn

# Copy project (excluding venv directory)
COPY . .

# PROD: For production, collect static files
# RUN python manage.py collectstatic --noinput

# Run the application
EXPOSE 8000

# PROD: For development server (change for production)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# PROD: For production, use gunicorn instead:
# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi:application"] 