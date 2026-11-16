# Python Flask Login Application

## Project Overview

A user authentication application developed using Python, Flask and SQLite. The application supports user registration, secure password hashing, login authentication, session management and logout functionality.

The application is containerized using Docker to provide a repeatable build and run process.

## Technologies Used

- Python 3.12
- Flask
- SQLite
- Werkzeug
- Docker
- Git and GitHub

## Project Features

- User registration
- Secure password hashing
- Login authentication
- Protected dashboard
- Flask session management
- Logout functionality
- SQLite database persistence using Docker volumes

## Project Structure

```text
python-login-app/
├── templates/
│   ├── register.html
│   ├── login.html
│   └── dashboard.html
├── data/
├── app.py
├── database.py
├── init_db.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .gitignore
└── README.md
```

## Prerequisites

Install the following:

- Git
- Docker Desktop or Docker Engine

## Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd python-login-app
```

## Build the Docker Image

```bash
docker build -t python-login-app .
```

## Run the Application

```bash
docker run -d \
  -p 5000:5000 \
  -v flask_data:/app/data \
  --name flask-container \
  python-login-app
```

Open the application:

http://localhost:5000

## View Container Status

```bash
docker ps
```

## View Application Logs

```bash
docker logs flask-container
```

## Stop the Container

```bash
docker stop flask-container
```

## Remove the Container

```bash
docker rm flask-container
```

## Database Persistence

The application uses a Docker named volume called `flask_data`.

The volume is mounted at `/app/data` inside the container. This allows SQLite database records to persist when the container is removed and recreated.

To reuse the existing database, run the application again with the same volume:

```bash
docker run -d -p 5000:5000 \
  -v flask_data:/app/data \
  --name flask-container \
  python-login-app
```

## Author

Add your name here.

## Repository

Add your GitHub repository URL here.