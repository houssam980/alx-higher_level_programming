#!/usr/bin/python3
""" Script that lists all states from the database"""
from sys import argv
import MySQLdb


if __name__ == '__main__':

    # make a connection to the database
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states")

    rows = cur.fetchall()
    for i in rows:
        print(i)
        """closing connection"""
    cur.close()
    db.close()
