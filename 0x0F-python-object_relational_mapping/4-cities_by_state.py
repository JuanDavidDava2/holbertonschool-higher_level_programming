#!/usr/bin/python3
"""
Script that takes in arguments and displays all values.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    user, passwd, db = argv[1], argv[2], argv[3]
    db = MySQLdb.connect(host='localhost', user=user,
                              passwd=passwd, db=db, port=3306)
    cursor = db.cursor()
    cursor.execute("""SELECT cities.id, cities.name, states.name
              FROM cities, states WHERE cities.state_id = states.id
              ORDER BY cities.id""")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
