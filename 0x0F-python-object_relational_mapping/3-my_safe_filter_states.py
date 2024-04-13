#!/usr/bin/python3
"""display all values that match specified argument
   safe from SQL injections
"""


import MySQLdb as dbmod
from sys import argv

if __name__ == "__main__":
    """check name in table that match argument received"""

    db = dbmod.connect(host="localhost", port=3306,
                       user=argv[1], passwd=argv[2], db=argv[3])

    cur = db.cursor()

    col = argv[4]
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY \
                 %(name)s ORDER BY states.id", {'name': argv[4]})

    result = cur.fetchall()

    for row in result:
        print(row)
