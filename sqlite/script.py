import sqlite3

# Define connection and cursor

connection = sqlite3.connect('store_transactions.db')

cursor = connection.cursor()

# create stores table

command = """CREATE TABLE IF NOT EXISTS stores(store_id INTEGER PRIMARY KEY, location TEXT)
"""
# Primary key specifies the field store ID must be unique for each row in the table. This allows other table to
# reference or relate to it when they use ID as a foreign key attribute
cursor.execute(command)

# Create purchases tables

command2 = """CREATE TABLE IF NOT EXISTS
purchases(purchase_id INTEGER PRIMARY KEY, store_id INTEGER, total_cost FLOAT, FOREIGN KEY(store_id) REFERENCES 
stores(store_id))"""

cursor.execute(command2)

# add to stores
cursor.execute("INSERT INTO stores VALUES (21, 'Minneapolis, MN')")
cursor.execute("INSERT INTO stores VALUES (95, 'Chicago, IL')")
cursor.execute("INSERT INTO stores VALUES (64, 'Iowa City, IA')")

# add to purchases
cursor.execute("INSERT INTO purchases VALUES (54, 21, 15.49)")
cursor.execute("INSERT INTO purchases VALUES (23, 64, 21.12)")

# get results
cursor.execute("SELECT * FROM purchases")

results = cursor.fetchall()
print(results)

# update
cursor.execute("UPDATE purchases SET total_cost = 3.67 WHERE purchase_id = 54")

# delete cursor.execute("DELETE FROM purchases WHERE purchase_id = 54")
