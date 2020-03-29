#!/usr/bin/python3
"""
Script that takes in arguments and displays all values.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    user, passwd, db, state = argv[1], argv[2], argv[3], argv[4]
    db = MySQLdb.connect(host='localhost', user=user,
                              passwd=passwd, db=db, port=3306)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id")
    rows = cursor.fetchall()
    for row in rows:
        if (state == row[1]):
            print(row)
