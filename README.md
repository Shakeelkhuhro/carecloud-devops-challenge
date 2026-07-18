# CareCloud DevOps Infrastructure Challenge

![Docker](https://img.shields.io/badge/Docker-Compose-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-blue)
![NGINX](https://img.shields.io/badge/NGINX-Reverse%20Proxy-brightgreen)
![Prometheus](https://img.shields.io/badge/Prometheus-Monitoring-orange)
![Grafana](https://img.shields.io/badge/Grafana-Dashboards-F46800)
![GitHub Actions](https://img.shields.io/badge/CI-GitHub%20Actions-success)

> **Production-inspired DevOps infrastructure for deploying a containerized FastAPI application with Docker Compose, NGINX, PostgreSQL, Prometheus, Grafana, automated backups, and GitHub Actions CI.**

---

# Overview

This repository demonstrates a production-inspired DevOps environment for deploying a FastAPI backend using Docker Compose. It includes a reverse proxy, database, monitoring stack, automated backups, health checks, metrics, and CI validation.

Although lightweight enough to run locally, the architecture follows common production deployment patterns.

---

# Architecture

```text
                    Client
                       │
                       ▼
                ┌───────────────┐
                │     NGINX     │
                │ Reverse Proxy │
                └──────┬────────┘
                       │
                       ▼
                ┌───────────────┐
                │    FastAPI    │
                │  Backend API  │
                └──────┬────────┘
                       │
         ┌─────────────┴─────────────┐
         ▼                           ▼
   PostgreSQL                  Prometheus
                                      │
                                      ▼
                                  Grafana
```

# Technology Stack

| Layer | Technology |
|------|------------|
| Backend | FastAPI |
| Database | PostgreSQL 16 |
| Reverse Proxy | NGINX |
| Monitoring | Prometheus |
| Dashboards | Grafana |
| Container Runtime | Docker |
| Orchestration | Docker Compose |
| CI | GitHub Actions |
| Backup | Bash + pg_dump |

# Features

- Dockerized FastAPI backend
- PostgreSQL database
- NGINX reverse proxy
- Prometheus monitoring
- Grafana dashboards
- Health endpoint
- Metrics endpoint
- Environment-based configuration
- Automated PostgreSQL backup script
- GitHub Actions CI pipeline

# Project Structure

```text
infra-challenge/
├── backend/
├── monitoring/
├── nginx/
├── scripts/
├── backups/
├── .github/workflows/
├── docker-compose.yml
├── .env.example
├── .env
└── README.md
```

# Quick Start

```bash
git clone https://github.com/Shakeelkhuhro/Carecloud-Devops-Challenge.git
cd infra-challenge
cp .env.example .env
docker compose up --build -d
docker ps
```

# Services

| Service | URL |
|----------|-----|
| Application | http://localhost |
| Health | http://localhost/health |
| Metrics | http://localhost/metrics |
| Prometheus | http://localhost:9090 |
| Grafana | http://localhost:3000 |

Default Grafana credentials:

| Username | Password |
|----------|----------|
| admin | admin |

# Monitoring

```bash
curl http://localhost/metrics
```

# Health Check

```bash
curl http://localhost/health
```

Expected:

```json
{"status":"healthy"}
```

# Database

- PostgreSQL 16
- Database: `carecloud`
- User: `carecloud`

# Backup

```bash
./scripts/backup.sh
```

Backups are stored in `backups/`.

# CI/CD

GitHub Actions automatically:

- Checks out repository
- Builds Docker images
- Validates Docker Compose configuration

Workflow:

```text
.github/workflows/ci.yml
```

# Environment Variables

```env
POSTGRES_DB=carecloud
POSTGRES_USER=carecloud
POSTGRES_PASSWORD=carecloud

GRAFANA_USER=admin
GRAFANA_PASSWORD=admin
```

# Networking

Services communicate over an isolated Docker network using service names instead of IP addresses.

# Observability

- Application metrics
- Health monitoring
- Grafana dashboards
- Prometheus scraping

# Security Considerations

- Reverse proxy via NGINX
- Environment-based configuration
- Internal Docker networking
- Persistent storage
- Replace default credentials before production deployment

# Production Considerations

- Reverse proxy
- Health checks
- Metrics collection
- Monitoring dashboards
- Automated backups
- CI pipeline
- Environment configuration

# Troubleshooting

```bash
docker compose logs
docker compose restart
docker compose up --build -d
```

# Future Enhancements

- HTTPS (Let's Encrypt)
- Redis
- Loki
- Alertmanager
- Docker Secrets
- Multi-stage Docker builds
- Image scanning
- Kubernetes manifests
- Helm charts
- Terraform

# Author

**Shakeel Ahmed Khuhro**

*DevOps Engineer | Cloud & Infrastructure Enthusiast*
