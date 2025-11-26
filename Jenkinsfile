pipeline {
    agent any
<<<<<<< HEAD

    environment {
        APP_NAME = "devops-lab-app"
        IMAGE_NAME = "${APP_NAME}:latest"
        KIND_CLUSTER = "devops-lab"
        NAMESPACE = "devops-lab"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Unit Tests') {
            steps {
                dir('app') {
                    sh """
                        python3 -m pip install -r requirements.txt
                        pytest -q
=======
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
>>>>>>> c5b1e3239a975390b4d4bdd3bccfb3ef13d81772
                    """
                }
            }
        }
<<<<<<< HEAD

        stage('Build Docker Image') {
            steps {
                sh """
                    docker build -t ${IMAGE_NAME} app/
                """
            }
        }

        stage('Load Image into kind') {
            steps {
                sh """
                    kind load docker-image ${IMAGE_NAME} --name ${KIND_CLUSTER}
                """
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh """
                    kubectl apply -f k8s/namespace.yaml
                    kubectl apply -f k8s/deployment.yaml
                    kubectl apply -f k8s/service.yaml
                    kubectl rollout status deployment/${APP_NAME} -n ${NAMESPACE}
                """
            }
        }
    }

    post {
        success {
            echo "🔥 Deployment successful!"
        }
        failure {
            echo "❌ Build failed."
        }
=======
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
>>>>>>> c5b1e3239a975390b4d4bdd3bccfb3ef13d81772
    }
}

