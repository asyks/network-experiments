#!/usr/bin/env python

import http.client
import socket


def request(method, path='/'):
    conn = http.client.HTTPConnection('server', 8000)
    conn.putrequest(method, path)
    try:
        conn.endheaders()
    except socket.gaierror as err:
        raise socket.gaierror(
            err.args[0],
            '{}, encountered getaddrinfo() exception, '
            'is the target server running?'.format(
                err.args[1],
            ),
        )

    except ConnectionRefusedError as err:
        raise ConnectionRefusedError(
            err.args[0],
            '{}, check the server hostname.'.format(
                err.args[1],
            ),
        )

    else:
        resp = conn.getresponse()
        print(resp.status, resp.reason)


def main():
    request('GET')
    request('HEAD')


if __name__ == '__main__':
    main()
