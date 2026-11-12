#!/usr/bin/env bash
set -euo pipefail

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
IMAGE_NAME="cloud-devops-api"
IMAGE_TAG="${1:-0.1.0}"
IMAGE="${IMAGE_NAME}:${IMAGE_TAG}"
CLUSTER_NAME="cloud-devops-lab"
NAMESPACE="devops-lab"
KUBECONFIG_PATH="${HOME}/.kube/cloud-devops-lab.yaml"

sudo -v

sudo docker build -t "$IMAGE" "$PROJECT_DIR/app"
sudo kind load docker-image "$IMAGE" --name "$CLUSTER_NAME"

kubectl --kubeconfig "$KUBECONFIG_PATH" apply -f "$PROJECT_DIR/k8s/base/namespace.yaml"
kubectl --kubeconfig "$KUBECONFIG_PATH" apply -f "$PROJECT_DIR/k8s/base/api.yaml"

kubectl --kubeconfig "$KUBECONFIG_PATH" \
  -n "$NAMESPACE" set image deployment/cloud-devops-api api="$IMAGE"

kubectl --kubeconfig "$KUBECONFIG_PATH" \
  -n "$NAMESPACE" rollout status deployment/cloud-devops-api --timeout=120s

kubectl --kubeconfig "$KUBECONFIG_PATH" \
  -n "$NAMESPACE" get pods
