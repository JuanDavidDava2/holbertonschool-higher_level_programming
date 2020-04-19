#!/usr/bin/python3
"""Sends  a request to the URL and displays
the body of the response"""

from urllib import request, parse, error
from sys import argv
if __name__ == "__main__":
    try:
        with request.urlopen(argv[1]) as res:
            print(res.read().decode('utf-8'))
    except error.HTTPError as err:
        print("Error code:", err.code)
