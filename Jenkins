pipeline {
    agent {
        label 'windows'  // Ensure Jenkins runs this on a Windows agent
    }

    environment {
        PYTHON = 'C:\\Python39\\python.exe'  // Update with your Python installation path
    }

    stages {
        stage('Checkout Code') {
            steps {
                git 'https://github.com/Ankit-MS24/Framework_Setup_1.git'  // Replace with your actual repo
            }
        }

        stage('Setup Python Virtual Environment') {
            steps {
                bat 'python -m venv venv'
                bat 'venv\\Scripts\\activate && python -m pip install --upgrade pip'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'venv\\Scripts\\activate && pip install -r requirements.txt'
            }
        }

        stage('Run Selenium Tests') {
            steps {
                bat 'venv\\Scripts\\activate && pytest --junitxml=reports/results.xml'
            }
        }

        stage('Publish Test Results') {
            steps {
                junit 'reports/results.xml'
            }
        }

        stage('Archive Reports') {
            steps {
                archiveArtifacts artifacts: 'reports/*.xml', fingerprint: true
            }
        }
    }

    post {
        always {
            echo 'Cleaning up workspace'
            deleteDir()
        }
    }
}
