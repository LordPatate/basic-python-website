from datetime import date
from http.server import BaseHTTPRequestHandler, HTTPServer
import logging
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
        print(output, file=self.wfile)


def main():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MyHandler)
    httpd.serve_forever()


if __name__ == "__main__":
    main()
