pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/AlerEel/MLOps.git'
            }
        }
        stage('Data Processing') {
            steps {
                bat 'python3 model_preprocessing.py'
            }
        }
        stage('Train Model') {
            steps {
                bat 'python3 model_preparation.py'
            }
        }
        stage('Evaluate Model') {
            steps {
                bat 'python3 model_testing.py'
            }
        }
    }
}