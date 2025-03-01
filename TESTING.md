# Testing Guide

This document provides instructions on how to run tests for both the backend and frontend components of the project.

## Backend Tests

The backend uses Django's testing framework along with pytest for more advanced testing capabilities.

### Running Tests

To run the backend tests:

```bash
# Navigate to the backend directory
cd backend

# Run tests using Django's test runner
python manage.py test

# Or run tests using pytest
pytest

# Run tests with coverage
coverage run --source='.' manage.py test
coverage report
coverage html  # Generates HTML report in htmlcov/
```

### Test Structure

- `blog/tests.py`: Contains tests for the blog app, including:
  - Model tests: Verify the behavior of the BlogPost model
  - API tests: Test the REST API endpoints for proper permissions and functionality

## Frontend Tests

The frontend uses Vitest and Testing Library for component testing.

### Running Tests

To run the frontend tests:

```bash
# Navigate to the frontend directory
cd frontend

# Install dependencies if not already installed
npm install

# Run tests
npm test

# Run tests in watch mode
npm run test:watch

# Run tests with coverage
npm run test:coverage
```

### Test Structure

- `src/lib/components/*.test.ts`: Component tests
- Coverage reports are generated in the `coverage` directory

## CI/CD Integration

This project uses GitHub Actions for continuous integration. The workflow is defined in `.github/workflows/ci.yml` and includes:

1. Running backend tests
2. Running frontend tests
3. Generating coverage reports

The CI pipeline runs automatically on:
- Push to the main branch
- Pull requests to the main branch

## Writing New Tests

### Backend

1. Add test methods to existing test classes in `blog/tests.py` or create new test files
2. Follow Django's testing conventions:
   - Use `TestCase` for model tests
   - Use `APITestCase` for API tests

### Frontend

1. Create a new test file alongside the component you're testing with the `.test.ts` extension
2. Use the Testing Library to render and interact with components
3. Write assertions using Vitest's expect API

## Best Practices

1. Aim for high test coverage, especially for critical functionality
2. Write tests before implementing new features (TDD)
3. Keep tests fast and independent
4. Use meaningful test names that describe the expected behavior
5. Mock external dependencies when appropriate 