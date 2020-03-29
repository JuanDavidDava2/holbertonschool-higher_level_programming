#!/usr/bin/python3
"""
display states table where name matches the argument.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    user, passwd, db, state = argv[1], argv[2], argv[3], argv[4]
    db = MySQLdb.connect(host='localhost', user=user,
                              passwd=passwd, db=db, port=3306)
    cursor = db.cursor()
    cursor.execute("""SELECT * FROM states
      WHERE BINARY states.name = '{}' ORDER BY states.id""".format(state))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
