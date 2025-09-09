# my-devops-project
🎯 Goal of my Project

The goal is to demonstrate a complete CI/CD DevOps pipeline for a simple Python Flask web app using modern DevOps tools.

You’re showing how code moves from development → containerization → automation → deployment.

🛠️ Tools in Your Stack

Flask (Python app)

Your sample web app: a minimal API / web server.

GitHub

Stores source code (version control).

Docker

Containerizes the Flask app so it can run anywhere consistently.

Jenkins

Automates CI/CD pipeline: clone repo → build image → push to DockerHub → trigger deployment.

Ansible

Automates deployment of the Docker container to your server(s).

Kubernetes (K8s) (optional in your structure)

For scaling and managing the app in production clusters.



🚀 Workflow (End-to-End)

Developer pushes code → GitHub (main branch).

Jenkins triggers (via webhook or polling).

Jenkins runs pipeline (Jenkinsfile):

Clone repo.

Build Docker image.

Push image to DockerHub.

Run Ansible playbook to deploy/update container.

(Apply K8s manifests to deploy to cluster).

Users access Flask app via server IP / LoadBalancer.
