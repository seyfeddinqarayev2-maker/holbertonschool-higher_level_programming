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
        response.raise_for_status()  # Raise HTTPError if status >= 400
        json_data = response.json()
        print(json_data.get("id"))
    except requests.HTTPError as e:
        print("Error code:", response.status_code)
    except requests.RequestException as e:
        print("Request failed:", e)
#!/usr/bin/python3
