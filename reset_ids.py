import sqlite3

# Connect to the database
conn = sqlite3.connect("patients.db")
cursor = conn.cursor()

# 1. Delete all patient data
cursor.execute("DELETE FROM patients")

# 2. Reset the auto-increment ID counter
cursor.execute("DELETE FROM sqlite_sequence WHERE name='patients'")

conn.commit()
conn.close()

print("✅ All records deleted and ID reset to 1.")
