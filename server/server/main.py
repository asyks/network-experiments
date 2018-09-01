#!/usr/bin/env python

from http.server import HTTPServer, BaseHTTPRequestHandler
from http import HTTPStatus
import logging

import log


logger = logging.getLogger(__name__)


class MyHTTPRequestHandler(BaseHTTPRequestHandler):

    def _log_connection_info(self):
        logger.info(
            (
                self.address_string(),
                self.client_address,
                self.request.family.value,  # Either: Unix, INET, or INET6
                self.request.type.value,  # Either: Unix, INET, or INET6
                self.request.fileno(),  # file number of the socket object
                self.headers.as_string(),
            )
        )

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
