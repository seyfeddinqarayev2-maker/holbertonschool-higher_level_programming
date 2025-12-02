#!/usr/bin/python3
"""Fetch a URL and display the body or error code if HTTP status >= 400"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        response = requests.get(url)
        if response.status_code >= 400:
            print("Error code: {}".format(response.status_code))
        else:
            print(response.text)
    except requests.RequestException as e:
        print("Request failed:", e)
