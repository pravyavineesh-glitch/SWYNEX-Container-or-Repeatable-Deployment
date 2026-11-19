
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out source code from GitHub'
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Building Docker image'
                sh 'docker build -t python-login-app .'
            }
        }

        stage('Test') {
            steps {
                echo 'Testing database connection'
                sh 'docker run --rm python-login-app python test_db.py'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying Flask application'
                sh '''
                    docker rm -f flask-container || true
                    docker run -d \
                      --restart unless-stopped \
                      -p 5000:5000 \
                      -v flask_data:/app/data \
                      --name flask-container \
                      python-login-app
                '''
            }
        }
    }
}
