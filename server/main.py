#!/usr/bin/env python

from http.server import HTTPServer, BaseHTTPRequestHandler
from http import HTTPStatus


class MyHTTPRequestHandler(BaseHTTPRequestHandler):

    def _send_header_and_status(self, status=HTTPStatus.OK):
        self.send_response(status)
        self.end_headers()

    def do_HEAD(self):
        self._send_header_and_status()

    def do_GET(self):
        self._send_header_and_status()
        self.wfile.write(bytes('OK', 'utf-8'))


def main(server_class=HTTPServer, handler_class=MyHTTPRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


if __name__ == '__main__':
    main()
