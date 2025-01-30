pipeline {
    agent any
    tools {
        // Указываем имя Python, которое вы добавили в Global Tool Configuration
        python "C:\Users\User\AppData\Local\Programs\Python\Python39\python.exe"
    }
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