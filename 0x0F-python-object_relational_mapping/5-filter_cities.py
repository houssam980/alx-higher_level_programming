#!/usr/bin/python3
""" Script that lists all states from the database"""
from sys import argv
import MySQLdb


if __name__ == '__main__':

    """making database connection"""
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    curls = db.cursor()
    curls.execute("SELECT cities.id, cities.name FROM cities\
                INNER JOIN states ON cities.state_id = states.id\
                WHERE states.name = %s", [argv[4]])

    rws = curls.fetchall()
    joi = [ ]
    for lp in rws:
        joi.append(lp[1])
        print(", ".join(joi))
        """closing connection"""
    curls.close()
    db.close()

