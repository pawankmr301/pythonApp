#!/usr/bin/python

import mysql.connector
import sys

try:
    cnx = mysql.connector.connect(user='manager', password='Manager#123',
                              host='127.0.0.1',
                              database='users')

    mycursor = cnx.cursor()

    sql = "SELECT * FROM users WHERE name = %s"
    val = (sys.argv[1],)

    mycursor.execute(sql, val)

    records = mycursor.fetchall()

    print "<html>"
    print "<head><title>Search Results</title></head>"
    print "<body>"
    print '<table border="5" style="width: 70%" align="center" cellpadding="5">'

    print "<tr>"
    print "<th>" + "NAME" + "</th>"
    print "<th>" + "ADDRESS" + "</th>"
    print "<th>" + "Phone No." + "</th>"
    print "</tr>"

    for row in records:
        print "<tr>"
        print "<td>" + row[0] + "</td>"
        print "<td>" + row[1] + "</td>"
        print "<td>" + row[2] + "</td>"
        print "</tr>"

    print "</table>"
    print '<br><br><h2><b><u><a href="/index.html">Home</a></u></b></h2>'
    print "</body>"
    print "</html>"

except:
    print "<h1 style='color:blue'>" + "DB ERROR: User Retrieval Failed!" + "</h1>" + '<br><br><h2><b><u><a href="/index.html">Home</a></u></b></h2>'

cnx.close()
