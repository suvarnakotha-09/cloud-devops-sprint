import json
import os
from collections import Counter
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from threading import Lock

PORT = int(os.environ.get("PORT", "8080"))

REQUEST_COUNTS = Counter()
REQUEST_LOCK = Lock()


def record_request(route, status):
    with REQUEST_LOCK:
        REQUEST_COUNTS[(route, status)] += 1


class Handler(BaseHTTPRequestHandler):
    def send_json(self, status, payload):
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def send_metrics(self):
        record_request("metrics", 200)

        with REQUEST_LOCK:
            samples = sorted(REQUEST_COUNTS.items())

        lines = [
            "# HELP cloud_devops_api_requests_total Total HTTP requests handled by the API.",
            "# TYPE cloud_devops_api_requests_total counter",
        ]

        for (route, status), count in samples:
            lines.append(
                'cloud_devops_api_requests_total'
                f'{{route="{route}",status="{status}"}} {count}'
            )

        body = ("\n".join(lines) + "\n").encode("utf-8")
        self.send_response(200)
        self.send_header(
            "Content-Type",
            "text/plain; version=0.0.4; charset=utf-8",
        )
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path == "/health":
            record_request("health", 200)
            self.send_json(200, {"status": "ok", "service": "cloud-devops-api"})
        elif self.path == "/metrics":
            self.send_metrics()
        elif self.path == "/":
            record_request("root", 200)
            self.send_json(200, {"message": "Cloud DevOps API is running"})
        else:
            record_request("not_found", 404)
            self.send_json(404, {"error": "not found"})


if __name__ == "__main__":
    server = ThreadingHTTPServer(("0.0.0.0", PORT), Handler)
    print(f"Server listening on port {PORT}")
    server.serve_forever()
