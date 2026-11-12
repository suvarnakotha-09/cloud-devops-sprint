# cloud-devops-sprint
# Cloud DevOps Sprint
[![Application CI](https://github.com/suvarnakotha-09/cloud-devops-sprint/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/suvarnakotha-09/cloud-devops-sprint/actions/workflows/ci.yml)
[![Terraform Validation](https://github.com/suvarnakotha-09/cloud-devops-sprint/actions/workflows/terraform.yml/badge.svg?branch=main)](https://github.com/suvarnakotha-09/cloud-devops-sprint/actions/workflows/terraform.yml)
[![Kubernetes Validation](https://github.com/suvarnakotha-09/cloud-devops-sprint/actions/workflows/kubernetes.yml/badge.svg?branch=main)](https://github.com/suvarnakotha-09/cloud-devops-sprint/actions/workflows/kubernetes.yml)

A hands-on DevOps portfolio project demonstrating a secure local CI/CD workflow for a containerized Python health API deployed to Kubernetes with Kind.

## What This Project Demonstrates

- Git and GitHub workflow using SSH authentication
- Python API testing with `unittest`
- Docker containerization
- Kubernetes Deployment and Service configuration
- Readiness and liveness health probes
- Non-root container security configuration
- Local Kubernetes deployment with Kind
- GitHub Actions CI pipeline
- Secure handling of secrets through `.gitignore`

## Architecture

```text
Developer → GitHub → GitHub Actions CI
                    ├── Run Python tests
                    ├── Validate deployment script
                    └── Build Docker image

Developer → Docker → Kind Kubernetes cluster → cloud-devops-api pods
## Observability

The API exposes Prometheus-compatible request metrics at:

```text
GET /metrics
