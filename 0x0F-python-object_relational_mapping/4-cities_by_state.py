#!/usr/bin/python3
"""
list all 'cities' from database 'hbtn_0e_4_usa'
sorted in ascending order by id
"""

import MySQLdb as dbmod
from sys import argv

if __name__ == "__main__":
    """list all cities from database"""

    db = dbmod.connect(host="localhost", port=3306, user=argv[1],
                       passwd=argv[2], db=argv[3])

    cur = db.cursor()

    cur.execute("SELECT cities.id, cities.name, states.name \
                 FROM cities JOIN states ON cities.state_id = states.id \
                 ORDER BY cities.id ASC")

    result = cur.fetchall()

    for row in result:
        print(row)
