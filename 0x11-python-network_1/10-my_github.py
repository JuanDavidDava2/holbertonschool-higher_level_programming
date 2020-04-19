#!/usr/bin/python3
"""
Task 10 - Use the Github API to display a user's ID
"""
import requests
from sys import argv

if __name__ == '__main__':
    r = requests.get('https://api.github.com/user', auth=(argv[1], argv[2]))
    print(r.json().get('id'))
