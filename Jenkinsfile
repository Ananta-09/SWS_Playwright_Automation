pipeline {
    agent any

    stages {
        stage('Verify Jenkins') {
            steps {
                echo 'Jenkins pipeline is running successfully!'
            }
        }

        stage('Check Python') {
            steps {
                bat '"C:\\Users\\ananta.nayak\\Desktop\\SWSPlaywrightAutomation\\venv\\Scripts\\python.exe" --version'
            }
        }
    }
}