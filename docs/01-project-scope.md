# Cloud DevOps Reference Project

## Objective
Build a secure, non-production DevOps reference project that demonstrates containerization, Kubernetes deployment, Infrastructure as Code, CI/CD, monitoring, and Azure DevOps practices.

## Project Approach
- Start locally with Docker and Kind Kubernetes.
- Use Git for version control.
- Use Terraform for Infrastructure as Code.
- Create CI/CD workflows after the application is ready.
- Use Azure DevOps concepts and templates only in an authorized sandbox environment.
- Never store passwords, API keys, Azure credentials, or secrets in Git.

## Planned Tools
- Linux
- Git and GitHub
- Docker
- Kubernetes using Kind
- Terraform
- GitHub Actions and Azure DevOps Pipelines
- Prometheus and Grafana
- Azure Key Vault guidance for authorized Azure environments

## Environments
- Development: Local computer
- Test: Local Kind Kubernetes cluster
- Cloud: Authorized Azure sandbox only
- Production: Not included

## Success Criteria
- A containerized application runs locally.
- The application deploys to a Kind Kubernetes cluster.
- Infrastructure is documented with Terraform templates.
- A CI/CD pipeline tests and builds the application.
- Security, rollback, monitoring, and deployment runbooks are included.
