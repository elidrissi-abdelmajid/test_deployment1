pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'test_deployment'
        DOCKER_TAG = "latest"
        DOCKER_USER = "mjid6"
        DOCKER_PASS ="dckr_pat_knjjAjvRy6Qsy1arF36wVnB2Wug"
    }

    stages {
        stage('clone the repository') {
            steps {
                // Pull the code from your Git repository
                git branch: 'master', url: 'https://github.com/elidrissi-abdelmajid/test_deployment1.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image
                    bat "docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} ."
                }
            }
        }
        stage('login to Docker') {
            steps {
                script {
                    // Build the Docker image
                    bat "docker login -u ${DOCKER_USER} -p ${DOCKER_PASS}"
            
                }
            }
        }
        stage("test the docker image"){
            steps{
                script{
                    bat "docker images"
                }
            }
        }
        stage('Push the image into docker hub') {
            steps {
                script {
                    // Build the Docker image
                    bat "docker push ${DOCKER_IMAGE}:${DOCKER_TAG}"
            
                }
            }
        }
        
    }

}
