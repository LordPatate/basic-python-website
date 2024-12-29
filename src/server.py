from datetime import date
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path


class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        template = Path("html/index.html").read_text()
        return template.format(
            date=date.today(),
            ip_address=self.address_string()
        )


def main():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MyHandler)
    httpd.serve_forever()


if __name__ == "__main__":
    main()
