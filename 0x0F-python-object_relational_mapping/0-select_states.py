#!/usr/bin/env python3
""" Program that gets all states sorted
in ascending ordered by states id """
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
    curs.execute("SELECT * FROM states ORDER BY id ASC")

    for row in curs.fetchall():
        print(row)

    curs.close()
    db.close()
