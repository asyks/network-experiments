#!/usr/bin/env python

import socket

from exceptions import InspectorTypeError


class SocketInspector(object):

    def __init__(self, request):
        if isinstance(request, socket.socket):
            self._r = request
        else:
            raise InspectorTypeError(
                'request is not of type {socket_type}'.format(
                    type(socket.socket)
                )
            )

    @property
    def socket_info(self):
        socket_info = {}

        sock_family = getattr(self._r, 'family')
        if sock_family and isinstance(sock_family, socket.AddressFamily):
            # Address Family e.g. Unix, INET, INET6
            socket_info['family'] = sock_family.name
        else:
            socket_info['family'] = NotImplemented

        sock_type = getattr(self._r, 'type')
        if sock_type and isinstance(sock_type, socket.SocketKind):
            # Socket type e.g. Stream, Datagram, Raw
            socket_info['type'] = sock_type.name
        else:
            socket_info['type'] = NotImplemented

        get_sock_num = getattr(self._r, 'fileno')
        if get_sock_num and callable(get_sock_num):
            # File number of the socket object
            socket_info['num'] = get_sock_num()
        else:
            socket_info['num'] = NotImplemented

        return socket_info
