import mysql.connector

dataBase = mysql.connector.connect(

    host = 'localhost',
    user = 'root',
    passwd = 'Bubblegum33@!',

	)

#prepare a cursor object
cursorObject = dataBase.cursor()

#Create a database
cursorObject.execute("CREATE DATABASE acs")

print("All Done!")