import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect("patients.db")
cursor = conn.cursor()

# Delete all records from the table
cursor.execute("DELETE FROM patients")
conn.commit()
conn.close()

print("✅ All records deleted from patients.db. You can now insert fresh encrypted data.")
