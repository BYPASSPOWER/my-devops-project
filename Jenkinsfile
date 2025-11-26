pipeline {
    agent any

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
                    """
                }
            }
        }

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
        always {
            echo "Pipeline completed: ${currentBuild.currentResult}"
        }
    }
}

