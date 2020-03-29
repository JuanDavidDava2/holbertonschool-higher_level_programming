#!/usr/bin/python3
"""
lists all cities of that state.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    user, passwd, db, state = argv[1], argv[2], argv[3], argv[4]
    db = MySQLdb.connect(host='localhost', user=user,
                              passwd=passwd, db=db, port=3306)
    cursor = db.cursor()
    cursor.execute("""SELECT cities.name FROM cities JOIN states ON
                 states.id = cities.state_id WHERE states.name=%s""", (state,))
    rows = cursor.fetchall()
    listr = []
    for row in rows:
        listr.append(row[0])
    print(", ".join(listr))
