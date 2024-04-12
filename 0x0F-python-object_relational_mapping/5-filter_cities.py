#!/usr/bin/python3
"""
takes name of a state as argument and
list all cities of that state
using database 'hbtn_0e_4_usa'
"""

import MySQLdb as dbmod
from sys import argv

if __name__ == "__main__":
    """list cities in a state"""

    db = dbmod.connect(host="localhost", port=3306, user=argv[1],
                       passwd=argv[2], db=argv[3])

    cur = db.cursor()

    state = argv[4]
    query = "SELECT cities.id, cities.name \
             FROM cities JOIN states ON cities.state_id = states.id \
             WHERE states.name LIKE BINARY '%s' \
             ORDER BY cities.id ASC" % (state)

    cur.execute(query)

    result = cur.fetchall()

    if result is not None:
        print(", ".join([row[1] for row in result]))
