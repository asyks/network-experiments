#!/usr/bin/env python

from http.server import HTTPServer, BaseHTTPRequestHandler
from http import HTTPStatus
import logging

import log
from request_inspect import SocketInspector


logger = logging.getLogger(__name__)


class MyHTTPRequestHandler(BaseHTTPRequestHandler):

    def _log_connection_info(self):
        # Print the request headers
        try:
            headers = self.headers.as_string()
        except AttributeError:
            pass
        else:
            logger.info('Request headers: %s', headers)

        # Print the client ipaddress and port
        try:
            addr_str, port = self.client_address
        except TypeError:
            pass
        else:
            logger.info('Client address and port: %s:%s', addr_str, port)

        # Retrieve and print info on the connections socket
        sock_inspector = SocketInspector(self.request)
        sock_info = sock_inspector.socket_info
        logger.info('Socket info: %s', sock_info)

    def _send_header_and_status(self, status=HTTPStatus.OK):
        self.send_response(status)
        self.end_headers()

    def do_HEAD(self):
        self._send_header_and_status()

    def do_GET(self):
        self._log_connection_info()
        self._send_header_and_status()
        self.wfile.write(bytes('OK', 'utf-8'))


def main(server_class=HTTPServer, handler_class=MyHTTPRequestHandler):
    # Setup logger
    log.init_logger()
    # Run Server
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


if __name__ == '__main__':
    main()
