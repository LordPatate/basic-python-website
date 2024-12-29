from datetime import date
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path


class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        address = self.address_string()
        template = Path("html/index.html").read_text()
        output = template.format(
            date=date.today(),
            ip_address=address
        )
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        _ = self.wfile.write(bytes(output, encoding="utf-8"))


def main():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MyHandler)
    httpd.serve_forever()


if __name__ == "__main__":
    main()
