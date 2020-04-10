#!/bin/bash
# sends a GET request to the URL, and displays the body of the response
curl -s "$1" -XPOST -d "email=hr@holbertonschool.com" -d "subject=I will always be here for PLD"
