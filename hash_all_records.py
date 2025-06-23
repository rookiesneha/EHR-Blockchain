import sqlite3
import hashlib

# Connect to the encrypted patient database
conn = sqlite3.connect("patients.db")
cursor = conn.cursor()

# Fetch all encrypted patient records
cursor.execute("""
    SELECT id, name, age, diagnosis, contact, address, medication_history, test_results, insurance_id
    FROM patients
""")
rows = cursor.fetchall()
conn.close()

if not rows:
    print("⚠️ No patient records found in the database.")
else:
    print("\n✅ SHA-256 Hashes of All Encrypted Records:")
    for row in rows:
        record_id = row[0]
        fields = row[1:]
        combined = ''.join(str(field) for field in fields).encode('utf-8')
        sha256_hash = hashlib.sha256(combined).hexdigest()
        print(f"Record ID {record_id}: 0x{sha256_hash}")