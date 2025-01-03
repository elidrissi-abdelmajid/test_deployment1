pipeline {
    agent any
    environment {
        DOCKER_IMAGE = 'test_deployment'
        DOCKER_TAG = "v5"
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
        stage('login to Docker') {
            steps {
                script {
                    // Build the Docker image
                    bat "docker login -u ${DOCKER_USER} -p ${DOCKER_PASS}"
            
                }
            }
        }
        stage('remove the old image') {
            steps {
                // Pull the code from your Git repository
                bat "docker rmi mjid6/${DOCKER_IMAGE}:latest --force"
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image
                    bat "docker build -t mjid6/${DOCKER_IMAGE}:${DOCKER_TAG} ."
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
                    bat "docker push mjid6/${DOCKER_IMAGE}:${DOCKER_TAG}"            
                }
            }
        }
        stage('deploy the image in k8s') {
            steps {
                script {
                // Apply the deployment YAML 
                bat "kubectl apply -f deployment.yaml --validate=false --kubeconfig=C:\\Users\\USER\\.kube\\config"
    
                // Force update the deployment with the new image
                bat "kubectl set image deployment/test-deployment test-container=mjid6/${DOCKER_IMAGE}:${DOCKER_TAG} --kubeconfig=C:\\Users\\USER\\.kube\\config"
    
                // Wait for the deployment to become ready
                bat "kubectl rollout status deployment/test-deployment --kubeconfig=C:\\Users\\USER\\.kube\\config"
    
                // Check services
                bat "kubectl get services --kubeconfig=C:\\Users\\USER\\.kube\\config"
    
                // Check the status of the Pods
                bat "kubectl get pods --selector=app=test-deployment --kubeconfig=C:\\Users\\USER\\.kube\\config"
    
                // Print node IPs
                bat "kubectl get nodes -o wide --kubeconfig=C:\\Users\\USER\\.kube\\config"
    
                // Port forward (if required to test locally)
                bat "kubectl port-forward service/test-service 8082:80 --kubeconfig=C:\\Users\\USER\\.kube\\config"
                }
            }
        }    
    }
}