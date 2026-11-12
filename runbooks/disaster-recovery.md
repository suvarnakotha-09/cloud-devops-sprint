# Local Kind Disaster Recovery Runbook

## Scope

This runbook applies only to the local `cloud-devops-lab` Kind cluster.

Do not use these steps for production systems.

## Recovery Conditions

Use this runbook only when:

- The Kind cluster cannot be reached.
- The Kubernetes control plane is unavailable.
- The local cluster has been intentionally deleted.
- Deployment recovery cannot be completed with `kubectl rollout undo`.

## Initial Checks

```bash
sudo kind get clusters

kubectl --kubeconfig "$HOME/.kube/cloud-devops-lab.yaml" \
  get nodes
