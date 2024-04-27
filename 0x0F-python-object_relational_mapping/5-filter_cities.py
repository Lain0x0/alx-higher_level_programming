#!/usr/bin/python3
"""This is a comment 2 """
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])

    curs = db.cursor()
    curs.execute("SELECT cities.name FROM cities\
                    JOIN states ON cities.state_id = states.id\
                    AND states.name = '{:s}'\
                    ORDER BY cities.id ASC".format(sys.argv[4]))

    li = []
    for i in c.fetchall():
        li.append(i[0])

    print(", ".join(li))

    curs.close()
    db.close()
