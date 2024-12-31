pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'fastapi-hello-world'
    }

    stages {
        stage('Checkout') {
            steps {
                // Pull the code from your Git repository
                git 'https://github.com/your-repo/fastapi-hello-world.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image
                    sh 'docker build -t $DOCKER_IMAGE .'
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    // Run the Docker container
                    sh 'docker run -d -p 8000:8000 $DOCKER_IMAGE'
                }
            }
        }

        stage('Clean up') {
            steps {
                script {
                    // Stop the container after the build
                    sh 'docker ps -q | xargs docker stop'
                    sh 'docker system prune -f'
                }
            }
        }
    }

    post {
        always {
            // Cleanup or notify actions
            echo 'Pipeline finished!'
        }
    }
}
