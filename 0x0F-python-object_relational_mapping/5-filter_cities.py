#!/usr/bin/python3
"""
script that takes in the name of a state as an argument and lists all cities
"""
import MySQLdb
from sys import argv


if __name__ == '__main__':
    """making databse connection"""
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    
    
    curs = db.cursor()
    curs.execute("SELECT cities.id, cities.name FROM cities\
                INNER JOIN states ON cities.state_id = states.id\
                WHERE states.name = %s", [argv[4]])

    rw = curs.fetchall()
    jer = []
    for iter in rw:
        jer.append(iter[1])
    print(", ".join(jer))
    
    
    """closing connection and excution"""
    curs.close()
    db.close()
