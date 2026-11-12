# Local Prometheus Monitoring Runbook

## Scope

This runbook applies only to the local Kind cluster and `devops-lab` namespace.

## Access Prometheus

Use an unused local port:

```bash
kubectl --kubeconfig "$HOME/.kube/cloud-devops-lab.yaml" \
  -n devops-lab port-forward service/prometheus 19090:9090
