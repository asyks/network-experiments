#!/usr/bin/env python

from http.server import HTTPServer, BaseHTTPRequestHandler
from http import HTTPStatus
import logging

import log
from request_inspect import SocketInspector


logger = logging.getLogger(__name__)


class MyHTTPRequestHandler(BaseHTTPRequestHandler):

    def _log_connection_info(self):

        headers = self.headers.as_string()  # TODO: handle excpetions here
        logger.info('Request headers: %s', headers)

        clnt_addr = self.client_address
        if isinstance(clnt_addr, tuple) and len(clnt_addr) == 2:
            addr_str = clnt_addr[0]
            port = clnt_addr[1]

            logger.info('Client address and port: %s:%s', addr_str, port)

        request = self.request
        sock_inspector = SocketInspector(request)
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
