#!/usr/bin/env python3

""" """

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
    curs.execute(" SELECT * FROM states WHERE name LIKE BINARY '{}'\
                    ORDER BY states.id ASC".format(sys.argv[4]))

    rows = curs.fetchall()
    for row in rows:
        print(row)
