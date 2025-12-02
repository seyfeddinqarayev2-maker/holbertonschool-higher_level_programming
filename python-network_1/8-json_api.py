#!/usr/bin/python3
"""Search a user by sending a POST request with a letter"""

import requests
import sys

if __name__ == "__main__":
    # Əgər argument verilməyibsə q boş olacaq
    q = sys.argv[1] if len(sys.argv) > 1 else ""

    url = "http://0.0.0.0:5000/search_user"
    data = {"q": q}

    try:
        response = requests.post(url, data=data)
        try:
            json_data = response.json()
            if json_data:
                print("[{}] {}".format(json_data.get("id"), json_data.get("name")))
            else:
                print("No result")
        except ValueError:
            print("Not a valid JSON")
    except requests.RequestException as e:
        print("Request failed:", e)
