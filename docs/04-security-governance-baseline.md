# Security and Governance Baseline

## Scope

This baseline applies to the future approved Azure sandbox environment and the current local DevOps project.

No Azure resources, identities, secrets, or policies have been changed by this project.

## Current Controls Implemented

| Control | Status |
| --- | --- |
| GitHub access through SSH key authentication | Implemented |
| Secrets, Terraform state, and local credentials excluded from Git | Implemented |
| Automated tests and Docker build in GitHub Actions | Implemented |
| Terraform formatting and validation in CI | Implemented |
| Non-root application container | Implemented |
| Kubernetes health probes and resource settings | Implemented |
| Deployment, rollback, and disaster-recovery runbooks | Implemented |

## Azure Identity and Access Baseline

- Use Microsoft Entra ID groups instead of direct user role assignments.
- Grant the least privilege needed at the narrowest possible scope.
- Limit `Owner` access and avoid subscription-wide Contributor access for daily work.
- Give a CI/CD workload identity access only to the approved sandbox Resource Group.
- Review privileged access regularly and use time-limited access where available.
- Use read-only roles for audits and architecture reviews.

## Secret Management Baseline

- Never store passwords, API keys, tokens, or connection strings in Git.
- Use Azure Key Vault for application secrets.
- Prefer managed identities or workload identity federation over stored credentials.
- Use Azure RBAC for Key Vault access.
- Separate Key Vaults by application and environment.
- Define an owner and rotation schedule for every secret.

## Governance and Cost Baseline

Required resource tags:

| Tag | Example |
| --- | --- |
| `environment` | `sandbox` |
| `project` | `cloud-devops-sprint` |
| `owner` | `suvarna` |
| `managed_by` | `terraform` |
| `cost_center` | `learning` |

Recommended controls:

- Start Azure Policy assignments in audit mode before enforcing deny rules.
- Restrict deployments to approved Azure regions.
- Require standard tags on new resources.
- Create a sandbox budget and cost alerts.
- Review Azure Advisor recommendations regularly.
- Store infrastructure changes in Git and review Terraform plans before approval.

## Change Approval Checklist

Before any Azure deployment:

1. Confirm the target subscription and Resource Group.
2. Confirm no secrets are included in the change.
3. Run `terraform fmt` and `terraform validate`.
4. Review the Terraform plan with an authorized reviewer.
5. Confirm rollback steps and ownership.
6. Obtain written approval before applying changes.
7. Record deployment evidence and final validation results.

