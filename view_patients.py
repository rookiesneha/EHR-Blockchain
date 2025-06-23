import sqlite3

conn = sqlite3.connect("patients.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM patients")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
