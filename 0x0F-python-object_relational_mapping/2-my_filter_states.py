#!/usr/bin/python3
"""
script that takes in an argument and displays all values in the states table
"""
import MySQLdb
from sys import argv


if __name__ == '__main__':
    """making databse connection"""
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    curs = db.cursor()
    usrN = "SELECT * FROM states WHERE name LIKE BINARY '{}'".format(argv[4])
    curs.execute(usrN)

    rw = curs.fetchall()
    for iter in rw:
        print(iter)
    # closing connection and excution
    curs.close()
    db.close()
