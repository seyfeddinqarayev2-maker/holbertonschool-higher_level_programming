#!/usr/bin/python3
"""Fetches X-Request-Id from a URL response header"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)
    print(response.headers.get("X-Request-Id"))
