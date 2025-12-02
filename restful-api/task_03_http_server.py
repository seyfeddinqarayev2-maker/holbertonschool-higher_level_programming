#!/usr/bin/python3
"""Simple API using http.server module"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json

HOST = "localhost"
PORT = 8000


class SimpleAPIHandler(BaseHTTPRequestHandler):
    """Custom HTTP request handler for our simple API"""

    def _send_headers(self, status_code=200, content_type="text/plain"):
        """Helper to send headers"""
        self.send_response(status_code)
        self.send_header("Content-type", content_type)
        self.end_headers()

    def do_GET(self):
        """Handle GET requests"""
        if self.path == "/":
            self._send_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        elif self.path == "/data":
            self._send_headers(content_type="application/json")
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode("utf-8"))
        elif self.path == "/status":
            self._send_headers()
            self.wfile.write(b"OK")
        else:
            self._send_headers(status_code=404)
            self.wfile.write(b"Endpoint not found")


def run(server_class=HTTPServer, handler_class=SimpleAPIHandler):
    """Run the HTTP server"""
    server_address = (HOST, PORT)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server at http://{HOST}:{PORT}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server.")
        httpd.server_close()


if __name__ == "__main__":
    run()
