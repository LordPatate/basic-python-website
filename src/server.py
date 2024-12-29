from datetime import date
from http.server import BaseHTTPRequestHandler, HTTPServer
import logging
from pathlib import Path


class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        address = self.address_string()
        logging.info("GET from %s", address)
        template = Path("html/index.html").read_text()
        return template.format(
            date=date.today(),
            ip_address=address
        )


def main():
    logging.basicConfig(level=logging.INFO)
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MyHandler)
    httpd.serve_forever()


if __name__ == "__main__":
    main()
