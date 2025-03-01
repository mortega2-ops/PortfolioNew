# Production Deployment Guide

This document outlines the key considerations and changes needed when deploying this application to a production environment.

## Architecture Changes

For production, the architecture should be modified as follows:

1. **Web Server**: Add Nginx as a reverse proxy to:
   - Handle SSL termination
   - Serve static files
   - Route requests to the appropriate services

2. **Database**:
   - Replace SQLite with PostgreSQL or another production-ready database
   - Set up proper backups and monitoring

3. **Application Servers**:
   - Replace Django's development server with Gunicorn/Uvicorn
   - Build the frontend as static files to be served by Nginx

## Docker Configuration Changes

### docker-compose.yml

Create a separate `docker-compose.prod.yml` file with:
- Production-specific environment variables
- No development volume mounts
- Database service
- Nginx service for reverse proxy
- Named volumes for persistent data

### Backend Dockerfile

For production:
1. Use Gunicorn instead of Django's development server
2. Collect static files during build
3. Set proper environment variables (DEBUG=False, etc.)
4. Add health checks

### Frontend Dockerfile

For production:
1. Use a multi-stage build:
   - First stage: build the static files
   - Second stage: use Nginx to serve the static files
2. Configure Nginx to work with the SPA routing

## Security Considerations

1. **Environment Variables**:
   - Never commit sensitive information to the repository
   - Use environment variables or secrets management
   - Consider using `.env` files (excluded from git)

2. **HTTPS**:
   - Set up SSL certificates (Let's Encrypt is a good option)
   - Configure HTTPS-only access
   - Set up proper HSTS headers

3. **Database**:
   - Use strong passwords
   - Limit network access
   - Regular backups

4. **Django Settings**:
   - Set `DEBUG=False`
   - Generate a new `SECRET_KEY`
   - Set proper `ALLOWED_HOSTS`
   - Configure CSRF and session security

## Deployment Checklist

Before deploying to production:

1. Update all dependencies to secure versions
2. Run security checks on your code
3. Test the production build locally
4. Set up monitoring and logging
5. Configure backups
6. Set up CI/CD pipelines if applicable

## Example Production Setup

```yaml
# docker-compose.prod.yml
services:
  backend:
    build:
      context: ./backend
      dockerfile: Dockerfile.prod
    environment:
      - DEBUG=False
      - SECRET_KEY=${SECRET_KEY}
      - DJANGO_ALLOWED_HOSTS=${DOMAIN}
      - DATABASE_URL=postgres://${DB_USER}:${DB_PASSWORD}@db:5432/${DB_NAME}
    depends_on:
      - db
    restart: unless-stopped

  frontend:
    build:
      context: ./frontend
      dockerfile: Dockerfile.prod
    restart: unless-stopped

  db:
    image: postgres:14
    volumes:
      - postgres_data:/var/lib/postgresql/data
    environment:
      - POSTGRES_PASSWORD=${DB_PASSWORD}
      - POSTGRES_USER=${DB_USER}
      - POSTGRES_DB=${DB_NAME}
    restart: unless-stopped

  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx/conf.d:/etc/nginx/conf.d
      - ./certbot/www:/var/www/certbot
      - ./certbot/conf:/etc/letsencrypt
      - static_volume:/var/www/static
    depends_on:
      - backend
      - frontend
    restart: unless-stopped

volumes:
  postgres_data:
  static_volume:
```

## Hosting Options

Consider these hosting options for your Docker containers:
- DigitalOcean App Platform
- AWS ECS/EKS
- Google Cloud Run
- Heroku
- Railway
- Render

Each platform has different pricing models and features, so choose based on your specific needs and budget. 