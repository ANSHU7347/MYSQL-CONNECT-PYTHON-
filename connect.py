import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="****",
  password="******",
  database="mydatabase"
)
 ###STEP 1
#mycursor = mydb.cursor()
  
#mycursor.execute("CREATE TABLE customer (name VARCHAR(255), address VARCHAR(255))")
#for i in mycursor:
    # print(i)

  ###STEP 2

#mycursor = mydb.cursor()
#sql = "INSERT INTO customer (name, address) VALUES (%s, %s)"
#val = ("John", "Highway 21")
#mycursor.execute(sql, val)

#mydb.commit()

#print(mycursor.rowcount, "record inserted.")


  #STEP 3

#mycursor = mydb.cursor()

#sql = "INSERT INTO customer (name, address) VALUES (%s, %s)"
#val = [
 #('Amy', 'Apple st 652'),
  #('Hannah', 'Mountain 21'),
  #('Michael', 'Valley 345'),
  #('Sandy', 'Ocean blvd 2'),
  #('Betty', 'Green Grass 1'),
  #('Richard', 'Sky st 331'),
  #('Susan', 'One way 98'),
  #('Vicky', 'Yellow Garden 2'),
#('Ben', 'Park Lane 38'),
 # ('William', 'Central st 954'),
  #('Chuck', 'Main Road 989'),
  #('Viola', 'Sideway 1633')
#]

#mycursor.executemany(sql, val)

#mydb.commit()

#print(mycursor.rowcount, "was inserted.")

###STEP 4
#
#mycursor = mydb.cursor()
#mycursor.execute("SELECT * FROM customer")

#myresult = mycursor.fetchall()

#for x in myresult:
 # print(x)

 ###STEP 5
#mycursor = mydb.cursor()

#sql = "SELECT * FROM customers WHERE address LIKE '%way%'"

#mycursor.execute(sql)

#myresult = mycursor.fetchall()

#for x in myresult:
  #print(x)

 ###STEP 6
#mycursor = mydb.cursor()

#sql = "SELECT * FROM customers ORDER BY name"

#mycursor.execute(sql)

#myresult = mycursor.fetchall()

#for x in myresult:
  #print(x)

 # #STEP 7

#mycursor = mydb.cursor()

#sql = "SELECT * FROM customers ORDER BY name DESC"

#mycursor.execute(sql)

#myresult = mycursor.fetchall()

#for x in myresult:
  #print(x)

  ###STEP 7
#mycursor = mydb.cursor()

#sql = "DELETE FROM customers WHERE address = 'Mountain 21'"

#mycursor.execute(sql)

#mydb.commit()

#print(mycursor.rowcount, "record(s) deleted")
###STEP 8
#mycursor = mydb.cursor()

#sql = "DROP TABLE customers"

#mycursor.execute(sql)
###STEP 9
#mycursor = mydb.cursor()

#sql = "UPDATE customer SET address = 'Canyon 123' WHERE address = 'Valley 345'"

#mycursor.execute(sql)

#mydb.commit()

#print(mycursor.rowcount, "record(s) affected")

##########STEP10
#mycursor = mydb.cursor()

#mycursor.execute("SELECT * FROM customer LIMIT 5")

##for x in myresult:
  #print(x)

#####STEP11
#mycursor = mydb.cursor()

#mycursor.execute("SELECT * FROM customer LIMIT 5 OFFSET 2")

#myresult = mycursor.fetchall()

#for x in myresult:
 # print(x)

 ###STEP12
mycursor = mydb.cursor()

sql = "SELECT \
  users.name AS user, \
  products.name AS favorite \
  FROM users \
  INNER JOIN products ON users.fav = products.id"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)








