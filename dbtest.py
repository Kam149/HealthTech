#!C:\Python37\python.exe

import mysql.connector as mysql

print("content-type:text/html")
print("")

cnn = mysql.connect(host="localhost",user="root",password="root",database="pythondb")

cr = cnn.cursor()

query = "select * from contact"

cr.execute(query)

#while True:
#	data = cr.fetchone()
#	if data is None:
#		break
#	print(data)

#data = cr.fetchmany(2)
#print(data)
#data = cr.fetchmany(2)
#print(data)
#data = cr.fetchmany(2)
#print(data)

#data = cr.fetchall()
#print(data)

data = cr.fetchone()
print(data)
data = cr.fetchmany(2)
print(data)

cnn.close()


