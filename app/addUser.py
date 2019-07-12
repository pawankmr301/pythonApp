#!/usr/bin/python

import mysql.connector
import sys

try:
    cnx = mysql.connector.connect(user='manager', password='Manager#123',
                              host='127.0.0.1',
                              database='users')

    mycursor = cnx.cursor()

    sql = "INSERT INTO users (name, address, phoneNo) VALUES (%s, %s, %s)"
    val = (sys.argv[1], sys.argv[2], sys.argv[3])

    mycursor.execute(sql, val)
    cnx.commit()

    print 'User Addition Successful!!<br><br><h2><b><u><a href="/index.html">Home</a></u></b></h2>'

except:
    print 'DB ERROR: User Addition Failed!!<br><br><h2><b><u><a href="/index.html">Home</a></u></b></h2>'

cnx.close()

