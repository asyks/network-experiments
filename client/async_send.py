#!/usr/bin/env python

import asyncio
import http
import json
import pprint
import sys
import time

import aiohttp

BASE_URL = "httpbin.org"

ops = ["get", "post", "put", "delete", "head"]


async def request(session, url, operation):
    method = getattr(session, operation)
    async with method(url) as response:
        print(response.status)
        return await response.text()


async def main():
    async with aiohttp.ClientSession() as session:
        for op in ops:
            print("Sleeping...")
            asyncio.sleep(2)
            content = await request(
                session, "http://" + BASE_URL + "/" + op, op
            )
            print(content)


def do_synchronous():
    for op in ops:
        print("Sleeping...")
        time.sleep(2)
        conn = http.client.HTTPConnection(BASE_URL, port=80)
        conn.request(op.upper(), "/" + op)
        resp = conn.getresponse()
        print(resp.status)
        try:
            content = json.loads(resp.read())
        except json.decoder.JSONDecodeError:
            pass
        else:
            pprint.pprint(content)


def do_asynchronous():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())


if __name__ == "__main__":
    test = sys.argv[1]
    start_time = time.time()
    if test == "sync":
        do_synchronous()
    elif test == "async":
        do_asynchronous()
    else:
        print("First arg must be 'sync' or 'async'")

    elapsed_time = time.time() - start_time
    print(elapsed_time)
