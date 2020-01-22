#!/usr/bin/python3
"""
Script that adds all arguments to a Python list
"""

import sys
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

if __name__ == "__main__":

    try:
        list = load_from_json_file("add_item.json")
    except FileNotFoundError:
        list = []
        list.extend(sys.argv[1:])
        save_to_json_file(list, "add_item.json")
