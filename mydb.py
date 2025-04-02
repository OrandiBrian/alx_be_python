import mysql.connector

# database connection details
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="belarandi",
    database="mydatabase"
)

# create a cursor object using the cursor() method
mycursor = mydb.cursor()

# create a table named 'customers' (if it doesn't exist)
mycursor.execute("""
    CREATE TABLE IF NOT EXISTS customers (
        id INT AUTO_INCREMENT PRIMARY KEY ,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL UNIQUE
        )
                 """)

print("Table created successfully!")

# insert some customer data
sql = "INSERT INTO customers (name, email) VALUES (%s, %s)"
val = ("John Doe", "john.doe@example.com")
mycursor.execute(sql, val)
mydb.commit()

print(mycursor.rowcount, "record(s) inserted.")

# read all customer data
mycursor.execute("SELECT * FROM customers")
myresult = mycursor.fetchall()

print("Customers:")
for customer in myresult:
    print(customer)

# update a customer's email
sql = "UPDATE customers SET email = %s WHERE id = %s"
val = ("updated.email@example.com", 1)
mycursor.execute(sql, val)
mydb.commit()

print(mycursor.rowcount, "record(s) updated.")

# read the updated customer data
mycursor.execute("SELECT * FROM customers WHERE id = 1")
myresult = mycursor.fetchone()

print("Updated customer:")
print(myresult)

# delete a customer
sql = "DELETE FROM customers WHERE id = 2"
mycursor.execute(sql)
mydb.commit()

print(mycursor.rowcount, "record(s) deleted.")

# close connections
mycursor.close()
mydb.close()