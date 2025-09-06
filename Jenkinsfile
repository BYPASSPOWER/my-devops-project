pipeline {
    agent any
    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/BYPASSPOWER/my-devops-project.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t BYPASSPOWER/flask-app:latest .'
            }
        }
        stage('Push to DockerHub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh 'echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin'
                    sh 'docker push <your-dockerhub-username>/flask-app:latest'
                }
            }
        }
        stage('Deploy with Ansible') {
            steps {
                sh 'ansible-playbook ansible/deploy.yml -i ansible/hosts'
            }
        }
    }
}
