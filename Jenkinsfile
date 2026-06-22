pipeline {
    agent any

    environment {
        PYTHONPATH = "${WORKSPACE}"
    }

    stages {
        stage('Initialize Environment') {
            steps {
                echo 'Setting up Python Virtual Environment...'
                sh 'python3 -m venv venv'
                sh './venv/bin/pip install -r requirements.txt'
            }
        }

        stage('Run Unit Tests') {
            steps {
                echo 'Executing Automated PyTest Suite...'
                // If tests fail, the pipeline stops and alerts are triggered
                sh './venv/bin/pytest tests/'
            }
        }

        stage('Simulate Build Artifact') {
            steps {
                echo 'Pipeline completed successfully. Packaging build metrics...'
                // Code to simulate log archiving or container registry push
                sh 'echo "Pipeline Run Status: Success" >> pipeline.log'
            }
        }
    }
    
    post {
        always {
            echo 'Archiving log artifacts...'
            archiveArtifacts artifacts: '*.log', allowEmptyArchive: true
        }
    }
}