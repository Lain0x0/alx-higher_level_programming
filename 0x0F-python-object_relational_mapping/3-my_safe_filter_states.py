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

    u = db.cursor()

    u.execute("SELECT * FROM states WHERE name LIKE %s", (sys.argv[4], ))

    x = u.fetchall()
    for row in x:
        print(row)

    u.close()
    db.close()
