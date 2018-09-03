#!/usr/bin/env python

import log


class SocketInspector(object):

    def __init__(self, request):
        self._r = request

    def non_socket_info(self):
        self.headers.as_string(),

    def socket_info(self):
        socket_info = {}

        sock_family = self._r.get('family')
        if sock_family and isinstance(sock_family, socket.AddressFamily):
            # Address Family e.g. Unix, INET, INET6
            socket_info['family'] = sock_family.name
        else:
            socket_info['family'] = NotImplemented

        sock_type = self._r.get('type')
        if sock_type and isinstance(sock_type, socket.SocketKind):
            # Socket type e.g. Stream, Datagram, Raw
            socket_info['type'] = sock_type.name
        else:
            socket_info['type'] = NotImplemented

        get_sock_num = self._r.get('fileno')
        if get_sock_num and callable(get_sock_num):
            # File number of the socket object
            socket_info['num'] = self.request.fileno()
        else:
            socket_info['num'] = NotImplemented

        return socket_info
