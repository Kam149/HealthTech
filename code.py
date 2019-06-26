import mysql.connector as mysql

def loadFile(filename):	
	fl = open("blocks/"+filename,"r")	
	return fl.read()

# select query
def fetchRecords(query):
	try:
		cnn = mysql.connect(host="localhost",user="root",password="",database="pythondb")
		cr = cnn.cursor()
		cr.execute(query)
		data = cr.fetchall()		
		return data
	except Exception as e:
		return False		
	finally:
		cnn.close()		

# dml query
def runQuery(query):	
	try:
		cnn = mysql.connect(host="localhost",user="root",password="",database="pythondb")
		cr = cnn.cursor()
		cr.execute(query)	
		cnn.commit()		
		return True
	except Exception as ex:		
		return False
	finally:
		cnn.close()			
		
	