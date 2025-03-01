# Portfolio Project

A personal portfolio website built with Django (backend) and SvelteKit (frontend).

## Features

- **Blog**: Display and manage blog posts
- **Portfolio**: Showcase projects and skills
- **Responsive Design**: Mobile-friendly interface
- **Docker Support**: Easy deployment with Docker

## Tech Stack

### Backend
- Django 4.2.7
- Django REST Framework
- Python 3.10

### Frontend
- SvelteKit 5.0
- TypeScript
- Vite

## Getting Started

### Prerequisites
- Docker and Docker Compose
- Git

### Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/portfolio.git
cd portfolio
```

2. Start the application with Docker Compose
```bash
docker-compose up
```

3. Access the application
   - Frontend: http://localhost:5173
   - Backend API: http://localhost:8000/api
   - Django Admin: http://localhost:8000/admin

### Development Setup (without Docker)

#### Backend Setup
1. Create and activate a virtual environment
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Run migrations
```bash
python manage.py migrate
```

4. Create a superuser
```bash
python manage.py createsuperuser
```

5. Start the development server
```bash
python manage.py runserver
```

#### Frontend Setup
1. Install dependencies
```bash
cd frontend
npm install
```

2. Start the development server
```bash
npm run dev
```

## Project Structure

```
portfolio/
├── backend/             # Django backend
│   ├── blog/            # Blog app
│   ├── portfolio/       # Main Django project
│   ├── venv/            # Python virtual environment
│   ├── manage.py        # Django management script
│   ├── requirements.txt # Python dependencies
│   └── Dockerfile       # Backend Docker configuration
├── frontend/            # SvelteKit frontend
│   ├── src/             # Source code
│   ├── static/          # Static assets
│   ├── package.json     # Node.js dependencies
│   └── Dockerfile       # Frontend Docker configuration
└── docker-compose.yml   # Docker Compose configuration
```

## Deployment

The application can be deployed using Docker Compose:

```bash
docker-compose -f docker-compose.yml up -d
```

## License

This project is licensed under the MIT License - see the LICENSE file for details. 