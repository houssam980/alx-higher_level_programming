#!/usr/bin/python3
""" script to list qll states """
import MySQLdb
from sys import argv


if __name__ == '__main__':
    
    """making database connection"""
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

 

    curs = db.cursor()
    curs.execute("SELECT * FROM states")

    rows = cur.fetchall()
    for iter in rw:
        print(iter)
        """close excution and db connection"""
    curs.close()
    db.close()
