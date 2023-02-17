import sqlite3

# Establish a connection and cursor
connection = sqlite3.connect("data.db")
cursor = connection.cursor()

# Query all data based on condition
cursor.execute("SELECT * FROM events WHERE band='Birds'")
rows = cursor.fetchall()
print(rows)

# Query certain data based on condition
cursor.execute("SELECT band, date FROM events WHERE band='Birds'")
rows = cursor.fetchall()
print(rows)

# Insert new rows
new_rows = [('Pig', 'Pig City', '2087.05.25'),
            ('Lang', 'Langs City', '2087.05.25')]

cursor.executemany("INSERT INTO events VALUES(?,?,?)", new_rows)
connection.commit()

# Query all data
cursor.execute("SELECT * FROM events")
rows = cursor.fetchall()
print(rows)