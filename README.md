# 🚀 GenAI-Powered Microservices Platform (DevOps Edition)

![Build Status](https://img.shields.io/badge/Build-Passing-success)
![Kubernetes](https://img.shields.io/badge/Orchestration-GKE-blue)
![Infrastructure](https://img.shields.io/badge/IaC-Terraform-purple)
![AI Model](https://img.shields.io/badge/Model-Gemini%201.5%20Pro-orange)
![GitOps](https://img.shields.io/badge/GitOps-ArgoCD-red)

## 📋 Project Overview
This project is a production-grade **Microservices Application** powered by **Google Gemini AI**. It demonstrates a complete **End-to-End DevOps Pipeline** utilizing Industry Standard tools.

The application consists of a **Streamlit Frontend** and a **FastAPI Backend** that communicates with Google's Vertex AI. The entire infrastructure is provisioned via **Terraform**, containerized with **Docker**, and deployed to **Google Kubernetes Engine (GKE)** using a **GitOps** workflow with **ArgoCD** and **Cloud Build**.

---

## 🏗️ Architecture

graph TD
    User[User] -->|HTTP/LB| Frontend[Streamlit Frontend]
    Frontend -->|REST API| Backend[FastAPI Backend]
    Backend -->|GRPC| VertexAI["Vertex AI (Gemini Pro)"]
    
    subgraph "Google Kubernetes Engine (GKE)"
        Frontend
        Backend
    end
    
    subgraph "DevOps Pipeline"
        Git[GitHub] -->|Push| CloudBuild[Cloud Build]
        CloudBuild -->|Build & Push| AR[Artifact Registry]
        ArgoCD[ArgoCD Controller] -->|Sync/Pull| AR
        ArgoCD -->|Deploy| GKE
    end

🛠️ Tech Stack
Category	                      Technology	                           USAGE
Cloud Provider	        Google Cloud Platform (GCP)	           Hosting & AI Services
Orchestration	          GKE (Kubernetes)	                     Container Management & Scaling
Infrastructure as Code	Terraform	                             Provisioning VPC, Subnets, GKE Cluster
CI/CD	                  Cloud Build & ArgoCD	                 Automated Testing & GitOps Deployment
AI/LLM	                Vertex AI (Gemini 1.5 Pro)	           Generative AI Logic
Backend	                Python (FastAPI)	                     Microservice API
Frontend	              Python (Streamlit)	                   User Interface
Security	              Workload Identity	                     Secure Service Account Impersonation
Containerization	      Docker	                               Artifact Registry Storage

Key Features
🤖 AI-Powered Chat: Real-time integration with Google Gemini 1.5 Pro for generating content and answering queries.

🔄 Fully Automated CI/CD: Changes pushed to GitHub trigger Cloud Build to build images, while ArgoCD automatically syncs Kubernetes to the latest state.

🛡️ Self-Healing Infrastructure: Utilizes ArgoCD's self-healing capabilities to automatically recreate deleted resources (e.g., Services/Deployments) in seconds.

🔐 Zero-Key Security: Uses Workload Identity to allow GKE Pods to authenticate with Vertex AI without storing JSON keys or secrets.

📉 Cost Optimized: Cluster utilizes auto-scaling and node-pool resizing to minimize idle costs

SCREENSHOTS
## SCREENSHOTS

1. Gen
<img src="https://github.com/user-attachments/assets/b9a80968-4ad6-4beb-9c9b-e4716f55b6f6" width="951">



A clean UI where users interact with the Gemini Model.

2. ARGOCD DESHBOARD (GITOPS)
<img width="1920" height="1200" alt="Screenshot 2025-11-27 004556" src="https://github.com/user-attachments/assets/3e39781d-4edb-4f4f-b635-6668ac8d9e8a" />


Visualizing the application state and sync status.

🚀 How to Run
Prerequisites
Google Cloud Project with Billing Enabled.

gcloud CLI, kubectl, and terraform installed.

Phase 1: Infrastructure (Terraform)
Provision the VPC and GKE Cluster.

Bash

cd infra
terraform init
terraform apply -auto-approve

Phase 2: Build & Deploy (Manual)
The cloudbuild.yaml handles the build process.

Bash

gcloud builds submit --config cloudbuild.yaml .
Phase 3: GitOps Setup (ArgoCD)
Install ArgoCD and connect it to the repository.

Bash

kubectl create namespace argocd
kubectl apply -n argocd -f [https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml](https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml)
kubectl apply -f argocd-app.yaml

🧠 Lessons Learned & Challenges
Kubernetes Caching: Encountered issues where GKE would not pull the latest image despite a successful build.

Solution: implemented imagePullPolicy: Always and added a rollout restart step in the CI pipeline.

Workload Identity: Moving from Service Account Keys to Workload Identity for better security posture.

Browser HTTP vs HTTPS: Debugged browser security policies blocking raw IP (HTTP) connections by enforcing explicit protocol usage or utilizing tunnels.

🔮 Future Enhancements
[ ] Implement Istio Service Mesh for canary deployments.

[ ] Add Prometheus & Grafana for monitoring pod metrics.

[ ] Migrate state storage to Redis for chat history memory.
