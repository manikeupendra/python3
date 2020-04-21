import pymysql

# Open database connection
db = pymysql.connect("localhost","root","root@123","college" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()


print ("Database version : %s " % data)
cursor.execute("SELECT * FROM college.student")
data = cursor.fetchone()
for d in data:
    print(d)

# print ("Database version : %s " % data)



# disconnect from server
db.close()