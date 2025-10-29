pipeline {
    agent any
    environment {
        AWS_REGION = "us-east-2"
        ECR_REPO   = "297997107385.dkr.ecr.${AWS_REGION}.amazonaws.com/inventory-app"
    }
    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    // Build Docker image and tag with Jenkins build number
                    docker.build("inventory-app:${env.BUILD_NUMBER}")
                }
            }
        }
        stage('Login to ECR') {
            steps {
                script {
                    // Login to AWS ECR
                    sh """
                    aws ecr get-login-password --region ${AWS_REGION} | \
                    docker login --username AWS --password-stdin ${ECR_REPO}
                    """
                }
            }
        }
        stage('Tag & Push Image') {
            steps {
                script {
                    // Tag Docker image for ECR and push
                    sh """
                    docker tag inventory-app:${BUILD_NUMBER} ${ECR_REPO}:${BUILD_NUMBER}
                    docker push ${ECR_REPO}:${BUILD_NUMBER}
                    """
                }
            }
        }
    }
}

