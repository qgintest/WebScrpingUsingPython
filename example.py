import sqlite3

# Establish connection
connection = sqlite3.connect("data.db")
cursor = connection.cursor()

# Query data
cursor.execute("SELECT * FROM events")
rows = cursor.fetchall()
print(rows)


# Insert data
# new_rows = [('Tigers', 'Tiger City', '2088.10.15'),
#             ('Humpty', 'Dumpty City', '2088.10.15')]
#
# cursor.executemany("INSERT INTO events VALUES(?, ?, ?)", new_rows)
#
# connection.commit()