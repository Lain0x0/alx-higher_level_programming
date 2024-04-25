#!/usr/bin/env python3

"""Listing all states with name start with N% """

if __name__ == "__main__":

    import MySQLdb
    import sys

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwrd=sys.argv[2],
            db=sys.argv[3]
            )
    curs = db.cursor()
    curs.execute("""
            SELECT * FROM states WHERE name
            LIKE BINARY '%N' ORDER BY states.id ASC;""")

    rows = curs.fetchall()
    for row in rows:
        print(row)
