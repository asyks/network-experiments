#!/usr/bin/env python

import requests


def main():
    response = requests.get('http://server:8000')
    print(response.status_code, response.content)


if __name__ == '__main__':
    main()