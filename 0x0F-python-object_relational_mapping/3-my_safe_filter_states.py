#!/usr/bin/python3
""" """
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])

    curs = db.cursor()
    curs.execute("SELECT * FROM states WHERE name LIKE %s", (sys.argv[4], ))
    rows = curs.fetchall()
    for row in rows:
        print(row)

    curs.close()
    db.close()
