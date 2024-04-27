#!/usr/bin/python3

""" Listing all states with name start with N% """

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
            )

    curs = db.cursor()
    curs.execute("SELECT * FROM states WHERE name\
            LIKE BINARY 'N%' ORDER BY id ASC")

    rows = curs.fetchall()
    for row in rows:
        print(row)

    curs.close()
    db.close()
