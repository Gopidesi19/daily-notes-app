# GCP 3‑Tier Daily Notes Application

This project demonstrates a **3‑tier cloud architecture** on Google Cloud.

Architecture:

User → API Gateway → Cloud Run (Flask App) → Firestore

Features:
- Enter daily notes
- Store notes in Firestore
- Retrieve notes from database
- CI/CD using Cloud Build
- Containerized using Docker

---

## Project Structure

gcp-daily-notes-app
│
├── app.py
├── requirements.txt
├── Dockerfile
├── cloudbuild.yaml
├── openapi.yaml
└── templates
    └── index.html

---

## 1. Login to GCP

gcloud auth login

Set project

gcloud config set project PROJECT_ID

---

## 2. Enable APIs

gcloud services enable run.googleapis.com
gcloud services enable cloudbuild.googleapis.com
gcloud services enable artifactregistry.googleapis.com
gcloud services enable apigateway.googleapis.com
gcloud services enable firestore.googleapis.com

---

## 3. Create Firestore Database

Console → Firestore → Create Database → Native Mode

---

## 4. Create Artifact Registry

gcloud artifacts repositories create notes-repo --repository-format=docker --location=us-central1

---

## 5. Build and Deploy

gcloud builds submit --config cloudbuild.yaml

---

## 6. Grant Firestore Access

Console → IAM

Add role:

Cloud Datastore User

to:

PROJECT_NUMBER-compute@developer.gserviceaccount.com

---

## 7. Deploy API Gateway

Create API in Console

Upload openapi.yaml

Replace:

CLOUD_RUN_URL

with your Cloud Run service URL.

---

## 8. Test Application

Open the API Gateway URL

Example UI:

My Daily Notes

Enter note → Save

Saved Notes
• Learn Kubernetes
• Study DevOps

---

## Technologies

- Flask
- Docker
- Cloud Run
- Firestore
- API Gateway
- Cloud Build