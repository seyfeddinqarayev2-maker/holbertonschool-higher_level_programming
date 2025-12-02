#!/usr/bin/python3
"""Displays your GitHub ID using Basic Authentication"""

import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]  # Personal access token

    url = "https://api.github.com/user"

    try:
        response = requests.get(url, auth=(username, token))
        if response.status_code == 200:
            json_data = response.json()
            print(json_data.get("id"))
        else:
            print(None)
    except requests.RequestException:
        print(None)
