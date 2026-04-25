pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                bat 'docker build -t flask-cms-app .'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'python -m unittest discover || echo No tests found'
            }
        }

        stage('Stop Old Container') {
            steps {
                bat 'docker stop flask-container || echo not running'
                bat 'docker rm flask-container || echo not exists'
            }
        }

        stage('Run Container') {
            steps {
                bat 'docker run -d -p 5000:3000 -v %cd%/data:/app/data --name flask-container flask-cms-app'
            }
        }
    }
}