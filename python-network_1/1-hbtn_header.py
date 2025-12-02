#!/usr/bin/python3
"""Fetches X-Request-Id from a URL response header"""

from urllib import request
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    with request.urlopen(url) as response:
        headers = response.info()
        x_request_id = headers.get("X-Request-Id")
        print(x_request_id)
