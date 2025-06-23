from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
import hashlib
from encryption import encrypt_text

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # needed for flash messages

# Route for home page (form)
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get form data
        name = request.form['name']
        age = int(request.form['age'])
        diagnosis = request.form['diagnosis']
        contact = request.form['contact']
        address = request.form['address']
        medication_history = request.form['medication_history']
        test_results = request.form['test_results']
        insurance_id = request.form['insurance_id']

        # Encrypt all fields
        enc_name = encrypt_text(name)
        enc_diagnosis = encrypt_text(diagnosis)
        enc_contact = encrypt_text(contact)
        enc_address = encrypt_text(address)
        enc_medication = encrypt_text(medication_history)
        enc_results = encrypt_text(test_results)
        enc_insurance = encrypt_text(insurance_id)

        # Save to database
        conn = sqlite3.connect('patients.db')
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO patients (name, age, diagnosis, contact, address, medication_history, test_results, insurance_id)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (enc_name, age, enc_diagnosis, enc_contact, enc_address, enc_medication, enc_results, enc_insurance))
        conn.commit()

        # Get last inserted record to generate hash
        record_id = cursor.lastrowid
        conn.close()

        fields = [enc_name, age, enc_diagnosis, enc_contact, enc_address, enc_medication, enc_results, enc_insurance]
        combined = ''.join(str(f) for f in fields).encode('utf-8')
        sha256_hash = hashlib.sha256(combined).hexdigest()

        full_hash = "0x" + sha256_hash
        print(f"✅ Full Hash (Record ID {record_id}): {full_hash}")

               # Append it to a file
        with open("hashes.txt", "a") as f:
            f.write(full_hash + "\n")

        # Show partial hash in browser (safe preview only)
        flash(f"✅ Patient added! Hash: 0x{sha256_hash[:6]}...{sha256_hash[-6:]}", "success")


    return render_template('index.html')

# ✅ This must be at the very end, not inside any function
if __name__ == '__main__':
    app.run(debug=True)
