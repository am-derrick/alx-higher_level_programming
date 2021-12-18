#!/usr/bin/python3
"""
lists all the states with a name starting with upper N from database hbtn_0e_0_usa
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQL.connect(host="localhost", port=3306, user=argv[1],
                       passwd=argv[2], db=argv[3], charset="utf8")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
