"""
script that takes in an argument and displays all values in the cities
"""
import MySQLdb
from sys import argv


if __name__ == '__main__':
    """making databse connection"""
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    curs = db.cursor()
    curs.execute("SELECT cities.id, cities.name, states.name FROM cities\
                INNER JOIN states ON cities.state_id = states.id\
                ORDER BY cities.id ASC")

    rw = curs.fetchall()
    for iter in rw:
        print(iter)
        """closing the connection and excution"""
    curs.close()
    db.close()
