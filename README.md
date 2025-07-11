﻿# 🛠️ Age Checker

A Flask-based web service for age verification, integrated with Prometheus for monitoring, Grafana for visualization, and a complete CI/CD pipeline using GitHub Actions and Render.

---

## Architecture Overview

```
Client (HTML/CSS)
|
Flask Web App (Python)
|
REST API Endpoints
|
Prometheus (Metrics)
|
Grafana (Dashboard)
```

- **Flask**: Core web application that calculates legal age based on birthdate.
- **Prometheus**: Collects and exposes application metrics such as request counts.
- **Grafana**: Displays real-time visualizations based on Prometheus metrics.
- **Docker**: Used to containerize all services.
- **GitHub Actions**: Handles CI (tests, linting, formatting, building).
- **Render**: Automatically deploys the app on push to the main branch (CD).

---

## 🔗 Live Deployment

Access the deployed application here:  
👉 [https://devops-final-project-968g.onrender.com/](https://devops-final-project-968g.onrender.com/)

---

## Setup Instructions

### Run with Docker Compose

```bash
docker-compose up --build
```

This will start the following services:

- Flask app (default on port 5000)
- Prometheus (on port 9090)
- Grafana (on port 3000)

### Key Endpoints

- `/check-age` – POST request with birth date to validate age
- `/health` – Health check endpoint
- `/metrics` – Prometheus metrics export

---

## CI Workflow

File: `.github/workflows/ci.yml`

Automatically runs on pull requests:

- **Checkout code**
- **Set up Python 3.11**
- **Install dependencies**
- **Run unit tests** (via `unittest`)
- **Lint check** (`flake8`)
- **Format check** (`black`)
- **Build Docker image**

---

## CD Workflow

File: `.github/workflows/cd.yml`

Triggered automatically on push to `main`:

1. Builds Docker image
2. Pushes it to DockerHub
3. Sends deploy request to Render via webhook

---

## Test Endpoint for CI/CD Demo

```python
# @main_bp.route("/cicd-test")
# def cicd_test():
#     return "CI/CD Pipeline Working!", 200
```

This endpoint is used for demonstrating live CI/CD. During presentation, uncomment it, commit the change, and push to `main` to trigger the pipeline.

---

## Project Structure

```
.
├── .github/
│   └── workflows/
│       ├── cd.yaml
│       └── ci.yaml
├── app/
│   ├── __init__.py
│   ├── app.py
│   ├── metrics.py
│   ├── static/
│   │   └── styles.css
│   └── templates/
│       └── index.html
├── tests/
│   └── test_app.py
├── docker-compose.yml
├── Dockerfile
├── grafana_dashboard_config.yml
├── grafana_dashboard.json
├── grafana_datasource.yml
├── prometheus.yml
├── requirements.txt
├── README.md

```
## Dashboard
![image](https://github.com/user-attachments/assets/e806e83d-49e8-4c6f-86a7-2cdbd95de3ea)

---

## Notes

- CD is triggered only on pushes to `main`
- Required GitHub Secrets:
  - `DOCKERHUB_USERNAME`
  - `DOCKERHUB_TOKEN`
  - `RENDER_DEPLOY_HOOK`

---
