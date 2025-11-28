#!/usr/bin/python3
"""Module to serialize and deserialize Python dictionaries using XML."""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize a Python dictionary to an XML file.

    Args:
        dictionary (dict): The dictionary to serialize.
        filename (str): The XML filename to write.
    """
    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """Deserialize an XML file into a Python dictionary.

    Args:
        filename (str): The XML filename to read.

    Returns:
        dict: The deserialized Python dictionary.
    """
    tree = ET.parse(filename)
    root = tree.getroot()
    result = {}

    for child in root:
        result[child.tag] = child.text

    return result
