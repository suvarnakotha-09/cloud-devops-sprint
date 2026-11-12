import json
import sys
import threading
import unittest
from http.client import HTTPConnection
from http.server import ThreadingHTTPServer
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "app"))

from app import Handler


class ApiTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()
        cls.port = cls.server.server_address[1]

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.thread.join()
        cls.server.server_close()

    def request_json(self, path):
        connection = HTTPConnection("127.0.0.1", self.port, timeout=2)
        connection.request("GET", path)
        response = connection.getresponse()
        body = json.loads(response.read().decode("utf-8"))
        connection.close()
        return response.status, body

    def request_text(self, path):
        connection = HTTPConnection("127.0.0.1", self.port, timeout=2)
        connection.request("GET", path)
        response = connection.getresponse()
        content_type = response.getheader("Content-Type")
        body = response.read().decode("utf-8")
        connection.close()
        return response.status, content_type, body

    def test_health_endpoint(self):
        status, body = self.request_json("/health")
        self.assertEqual(status, 200)
        self.assertEqual(body["status"], "ok")
        self.assertEqual(body["service"], "cloud-devops-api")

    def test_metrics_endpoint(self):
        status, content_type, body = self.request_text("/metrics")
        self.assertEqual(status, 200)
        self.assertIn("text/plain", content_type)
        self.assertIn("# HELP cloud_devops_api_requests_total", body)
        self.assertIn("# TYPE cloud_devops_api_requests_total counter", body)
        self.assertIn(
            'cloud_devops_api_requests_total{route="metrics",status="200"}',
            body,
        )

    def test_unknown_route_returns_not_found(self):
        status, body = self.request_json("/missing")
        self.assertEqual(status, 404)
        self.assertEqual(body["error"], "not found")


if __name__ == "__main__":
    unittest.main()
