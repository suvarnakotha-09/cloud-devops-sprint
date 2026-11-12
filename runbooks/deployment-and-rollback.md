# Local Kubernetes Deployment and Rollback Runbook

## Scope

This runbook applies only to the local Kind cluster named `cloud-devops-lab` and the `devops-lab` namespace.

Do not use these commands against production without written approval.

## Prerequisites

- Docker, Kind, kubectl, and Python are installed.
- The `cloud-devops-lab` Kind cluster is running.
- The repository working tree is reviewed before deployment.
- A new image version is used for every deployment.

## Pre-Deployment Checks

From the repository root:

```bash
git status
python3 -m unittest discover -s tests -v
kubectl --kubeconfig "$HOME/.kube/cloud-devops-lab.yaml" get nodes
