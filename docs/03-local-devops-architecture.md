# Cloud DevOps Sprint Architecture

## Current Architecture

```mermaid
flowchart TB
    Dev["Developer workstation"]
    Repo["GitHub repository"]
    CI["GitHub Actions CI"]
    AppCI["Python tests and Docker build"]
    TfCI["Terraform format and validation"]
    Docker["Local Docker image"]
    Kind["Kind Kubernetes cluster"]
    Namespace["devops-lab namespace"]
    Deployment["cloud-devops-api Deployment"]
    Service["ClusterIP Service"]
    Health["GET /health endpoint"]
    Terraform["Azure Resource Group module"]
    Azure["Azure sandbox - not deployed"]

    Dev --> Repo
    Repo --> CI
    CI --> AppCI
    CI --> TfCI
    Repo --> Terraform
    Terraform --> Azure
    Dev --> Docker
    Docker --> Kind
    Kind --> Namespace
    Namespace --> Deployment
    Deployment --> Service
    Service --> Health
```

## Components

| Component | Responsibility | Current Status |
| --- | --- | --- |
| GitHub | Source control and pull-request workflow | Active |
| GitHub Actions | Tests, Docker build, and Terraform validation | Active |
| Docker | Packages the Python health API | Active |
| Kind | Local Kubernetes learning environment | Active |
| Kubernetes | Runs two API replicas behind a Service | Active |
| Terraform | Defines an Azure Resource Group baseline | Validated only |
| Azure sandbox | Future approved infrastructure deployment | Not deployed |

## Security Boundaries

- No passwords, tokens, API keys, or client data are committed.
- The container runs as a non-root user.
- Kubernetes health probes verify application availability.
- Terraform state and local provider files are excluded from Git.
- Azure infrastructure will not be applied without approved sandbox access.

## Operational Documentation

- `runbooks/deployment-and-rollback.md`
- `runbooks/disaster-recovery.md`

