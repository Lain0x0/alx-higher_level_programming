#!/usr/bin/python3
"""This is a comment """
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
    [print(x) for x in u.fetchall()]

    u.close()
    db.close()
