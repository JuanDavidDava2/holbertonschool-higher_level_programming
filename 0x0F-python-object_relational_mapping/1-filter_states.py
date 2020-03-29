#!/usr/bin/python3
"""
lists all states with a name starting whit N.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    user, passwd, db = argv[1], argv[2], argv[3]
    db = MySQLdb.connect(host='localhost', user=user,
                              passwd=passwd, db=db, port=3306)
    cursor = db.cursor()
    cursor.execute("""SELECT * FROM states WHERE states.name
                   LIKE 'N%' ORDER BY states.id""")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
