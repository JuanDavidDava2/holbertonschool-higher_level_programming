#!/usr/bin/python3
"""Sends a request to the URL anddisplays the body of the response."""

import requests
from sys import argv

if __name__ == "__main__":
    res = requests.get(argv[1])
    if res.status_code >= 400:
        print("Error code:", res.status_code)
    else:
        print(res.text)
