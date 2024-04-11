#!/usr/bin/python3
""" Select states that start with a capital n from database"""


import MySQLdb
import sys

if __name__ == "__main__":
    """get state names that start with capital N"""

    db = mySQL.connect(
        host="localhost", user=sys.argv[1], port=3306,
        passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()

    cur.execute(
        "SELECT * FROM states WHERE name LIKE BINARY 'N%' \
         ORDER BY states.id ASC")

    rows = cur.fetchall()

    for row in rows:
        print(row)
