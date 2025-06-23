import sqlite3
import hashlib

# 🔐 Load hashes stored in blockchain from file
with open("hashes.txt", "r") as f:
    blockchain_hashes = [line.strip() for line in f.readlines()]

# Connect to the local patient database
conn = sqlite3.connect("patients.db")
cursor = conn.cursor()

# Fetch all patient records in order
cursor.execute("""
    SELECT id, name, age, diagnosis, contact, address, medication_history, test_results, insurance_id
    FROM patients
    ORDER BY id ASC
""")
rows = cursor.fetchall()
conn.close()

print("\n🔎 Checking for tampering against blockchain hashes:\n")

for i, row in enumerate(rows):
    record_id = row[0]
    fields = row[1:]  # skip ID
    combined = ''.join(str(field) for field in fields).encode('utf-8')
    hash_local = "0x" + hashlib.sha256(combined).hexdigest()

    if i < len(blockchain_hashes):
        if hash_local.lower() == blockchain_hashes[i].lower():
            print(f"✅ Record ID {record_id} (Blockchain Index {i}): Untampered.")
        else:
            print(f"❌ Record ID {record_id} (Blockchain Index {i}): TAMPERED!")
            print(f"   ↪ Expected: {blockchain_hashes[i]}")
            print(f"   ↪ Found:    {hash_local}")
    else:
        print(f"⚠️ Record ID {record_id} (Blockchain Index {i}): No blockchain hash found.")
