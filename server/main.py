#!/usr/bin/env python

import http

from http.server import HTTPServer, BaseHTTPRequestHandler


def main(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


if __name__ == '__main__':
    main()
