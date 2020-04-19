#!/usr/bin/python3
"""Send a POST request to the passed URL with email as a parameter"""

from urllib import parse, request
from sys import argv

if __name__ == '__main__':

    url = argv[1]
    values = {'email': argv[2]}

    data = parse.urlencode(values)
    data = data.encode('ascii')
    req = request.Request(url, data)
    with request.urlopen(req) as response:
        body = response.read()
    print(body.decode('utf-8'))
