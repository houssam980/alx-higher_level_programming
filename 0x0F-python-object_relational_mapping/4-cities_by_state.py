#!/usr/bin/python3
""" Script that lists all states from the database"""
from sys import argv
import MySQLdb


if __name__ == '__main__':

    """making database connection"""
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    curls = db.cursor()
    curls.execute("SELECT cities.id, cities.name, states.name FROM cities\
    INNER JOIN states ON cities.state_id = states.id\
    ORDER BY cities.id ASC")

    rws = curls.fetchall()
    for lp in rws:
        print(lp)
        """closing connection"""
    curls.close()
    db.close()

