pipeline {
    agent any

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
                bat 'pytest --html=reports/report.html --self-contained-html'
            }
        }

        stage('Publish Test Results') {
            steps {
                publishHTML (target: [
                    allowMissing: false,
                    alwaysLinkToLastBuild: true,
                    keepAll: true,
                    reportDir: 'reports',
                    reportFiles: 'report.html',
                    reportName: "Test Report"
                ])

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
