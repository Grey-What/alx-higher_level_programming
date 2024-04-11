#!/usr/bin/python3
""" list all states from database hbtn_0e_0_usa """


import MySQLdb
import sys

if __name__ == "__main__":
    """
    Access database and get names of states stored in it
    """
    db = MySQLdb.connect(
        host="localhost", port=3306, user=sys.argv[1],
        passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()

    cur.execute("SELECT * FROM states")

    rows = cur.fetchall()

    for row in rows:
        print(row)
