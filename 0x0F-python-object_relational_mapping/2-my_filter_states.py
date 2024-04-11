#!/usr/bin/python3
"""take an argument and search table of
   database where name matches argument
"""


import MySQLdb as dbmod
from sys import argv

if __name__ == "__main__":
    """searches for specific value in table field"""

    db = dbmod.connect(host="localhost", port=3306,
                       user=argv[1], passwd=argv[2], db=argv[3])

    cur = db.cursor()

    cur.execute(
        "SELECT * FROM states where name = '{}' \
         ORDER BY states.id ASC".format(argv[4]))

    result = cur.fetchall()

    for row in result:
        print(row)
