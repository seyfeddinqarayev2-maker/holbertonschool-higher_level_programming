#!/usr/bin/python3
"""Fetch and process posts from JSONPlaceholder using requests"""

import requests
import csv

API_URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():
    """Fetch all posts and print their titles."""
    response = requests.get(API_URL)
    print("Status Code:", response.status_code)

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post.get("title"))


def fetch_and_save_posts():
    """Fetch all posts and save them into posts.csv."""
    response = requests.get(API_URL)

    if response.status_code == 200:
        posts = response.json()

        # Prepare list of dictionaries with id, title, and body
        structured_posts = [
            {"id": post["id"], "title": post["title"], "body": post["body"]}
            for post in posts
        ]

        # Write to CSV
        with open("posts.csv", mode="w", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(structured_posts)
