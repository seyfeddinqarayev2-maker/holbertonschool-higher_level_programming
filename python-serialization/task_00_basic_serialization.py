#!/usr/bin/python3
"""Basic serialization module to save and load Python dictionaries as JSON."""

import json


def serialize_and_save_to_file(data, filename):
    """Serialize a Python dictionary and save it to a JSON file.

    Args:
        data (dict): The dictionary to serialize.
        filename (str): The output JSON filename.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Load and deserialize a JSON file to return a Python dictionary.

    Args:
        filename (str): The input JSON filename.

    Returns:
        dict: The deserialized Python dictionary.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
