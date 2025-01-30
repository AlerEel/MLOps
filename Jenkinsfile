pipeline {
    agent any
    stages {
//         stage('Install Dependencies') {
//             steps {
//                 script {
//                     // Указываем полный путь к Python
//                     bat 'C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python39\\python.exe -m pip install -r requirements.txt'
//                 }
//             }
//         }
        stage('Data Processing') {
            steps {
                script {
                    bat 'C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python39\\python.exe model_preprocessing.py'
                }
            }
        }
        stage('Train Model') {
            steps {
                script {
                    bat 'C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python39\\python.exe model_preparation.py'
                }
            }
        }
        stage('Evaluate Model') {
            steps {
                script {
                    bat 'C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python39\\python.exe model_testing.py'
                }
            }
        }
    }
}