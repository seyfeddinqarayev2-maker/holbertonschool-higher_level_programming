#!/usr/bin/python3
"""Module to convert CSV data to JSON format."""

import csv
import json


def convert_csv_to_json(csv_filename):
    """Convert a CSV file to JSON and save it to data.json.

    Args:
        csv_filename (str): The input CSV filename.

    Returns:
        bool: True if conversion successful, False otherwise.
    """
    try:
        with open(csv_filename, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            data_list = [row for row in reader]

        with open("data.json", "w", encoding="utf-8") as jsonfile:
            json.dump(data_list, jsonfile)

        return True
    except FileNotFoundError:
        return False
    except Exception:
        return False
