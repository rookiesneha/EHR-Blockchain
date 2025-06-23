import sqlite3

conn = sqlite3.connect("patients.db")
cursor = conn.cursor()

# Tampering diagnosis of record ID = 2
cursor.execute("""
    UPDATE patients
    SET diagnosis = 'ThisIsAFakeEncryptedDiagnosis123=='
    WHERE id = 2
""")

conn.commit()
conn.close()
print("⚠️ Tampering done: record ID 2 diagnosis altered.")
