import sqlite3
from decryption import decrypt_health_record

secret_key = "ThisIsASecretKey123"

conn = sqlite3.connect("patients.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM patients")
rows = cursor.fetchall()

print("\n--- Decrypted Patient Records ---\n")

for row in rows:
    try:
        record_id = row[0]
        name = decrypt_health_record(row[1], secret_key)
        age = row[2]
        diagnosis = decrypt_health_record(row[3], secret_key)
        contact = decrypt_health_record(row[4], secret_key)
        address = decrypt_health_record(row[5], secret_key)
        medication = decrypt_health_record(row[6], secret_key)
        test_results = decrypt_health_record(row[7], secret_key)
        insurance = decrypt_health_record(row[8], secret_key)
        timestamp = row[9] if len(row) > 9 else ""

        print(f"ID: {record_id}")
        print(f"Name: {name}")
        print(f"Age: {age}")
        print(f"Diagnosis: {diagnosis}")
        print(f"Contact: {contact}")
        print(f"Address: {address}")
        print(f"Medication History: {medication}")
        print(f"Test Results: {test_results}")
        print(f"Insurance ID: {insurance}")
        if timestamp:
            print(f"Timestamp: {timestamp}")
        print("-" * 50)
    except Exception as e:
        print(f"⚠️ Error decrypting record ID {row[0]}: {e}")

conn.close()