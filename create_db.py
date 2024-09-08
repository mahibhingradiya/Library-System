import MySQLdb as db2

db1 = db2.connect(host="Localhost",user="root",password="",db="LMS")
cursor=db1.cursor()
 
sql='''CREATE TABLE Library(id INT AUTO_INCREMENT PRIMARY KEY,
                           title VARCHAR(45) NULL,
                           author VARCHAR(45) NULL,
                           publisher VARCHAR(45) NULL,
                           edition VARCHAR(45) NULL,
                           price VARCHAR(45) NULL
                        
  
  )'''
 
cursor.execute(sql)

#closing the connection
db1.close()


