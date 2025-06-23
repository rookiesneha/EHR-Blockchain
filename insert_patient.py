import sqlite3
from datetime import datetime
from encryption import encrypt_text

name = input("Name: ")
age = input("Age: ")
diagnosis = input("Diagnosis: ")
contact = input("Contact: ")
address = input("Address: ")
med_history = input("Medication History: ")
test_results = input("Test Results: ")
insurance_id = input("Insurance ID: ")
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Encrypt using consistent encryption
enc_name = encrypt_text(name)
enc_diagnosis = encrypt_text(diagnosis)
enc_contact = encrypt_text(contact)
enc_address = encrypt_text(address)
enc_med_history = encrypt_text(med_history)
enc_test_results = encrypt_text(test_results)
enc_insurance_id = encrypt_text(insurance_id)

# Store in database
conn = sqlite3.connect('patients.db')
cursor = conn.cursor()
cursor.execute('''
    INSERT INTO patients (name, age, diagnosis, contact, address, medication_history, test_results, insurance_id, timestamp)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
''', (enc_name, age, enc_diagnosis, enc_contact, enc_address, enc_med_history, enc_test_results, enc_insurance_id, timestamp))
conn.commit()
conn.close()
print("✅ Patient record inserted successfully (with all fields encrypted).")