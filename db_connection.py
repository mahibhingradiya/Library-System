import MySQLdb as db2
	
db1 = db2.connect(host ="localhost",user = "root",password = "")
                  						
cursor = db1.cursor()
cursor.execute("DROP database IF EXISTS LMS")

#Preparing query to create a database
sql = "CREATE database LMS";

#Creating a database
cursor.execute(sql)

#Retrieving the list of databases
print("List of databases: ")
cursor.execute("SHOW DATABASES")
print(cursor.fetchall())

#Closing the connection
db1.close()