pipeline {
    agent any

    environment {
        IMAGE_NAME = 'jenkins-auto-deployment'
        CONTAINER_NAME = 'jenkins-auto-deployment'
        APP_PORT = '5000'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install --upgrade pip'
                bat 'python -m pip install -r app/requirements.txt'
                bat 'python -m pip install pytest'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'python -m pytest tests -v'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t %IMAGE_NAME%:%BUILD_NUMBER% .'
                bat 'docker tag %IMAGE_NAME%:%BUILD_NUMBER% %IMAGE_NAME%:latest'
            }
        }

        stage('Deploy to Production') {
            steps {
                bat 'docker rm -f %CONTAINER_NAME% || exit /b 0'
                bat 'docker run -d --name %CONTAINER_NAME% -p %APP_PORT%:5000 -e APP_VERSION=%BUILD_NUMBER% -e ENVIRONMENT=production %IMAGE_NAME%:latest'
            }
        }

        stage('Health Check') {
            steps {
                bat 'python -c "import urllib.request; r=urllib.request.urlopen(\'http://localhost:%APP_PORT%/health\', timeout=10); print(r.read().decode()); assert r.status == 200"'
            }
        }
    }

    post {
        success {
            echo 'Deployment completed successfully.'
        }
        failure {
            echo 'Pipeline failed. Check the Jenkins console output.'
        }
        always {
            echo 'CI/CD pipeline finished.'
        }
    }
}
