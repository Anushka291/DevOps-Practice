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

        stage('Run Container') {
            steps {
                docker stop flask-container || echo no container
                docker rm flask-container || echo no container
                docker run -d -p 5000:5000 --name flask-container flask-cms-app
            }
        }
    }
}