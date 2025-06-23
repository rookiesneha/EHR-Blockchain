import sqlite3

conn = sqlite3.connect('patients.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS patients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        diagnosis TEXT,
        contact TEXT,
        address TEXT,
        medication_history TEXT,
        test_results TEXT,
        insurance_id TEXT,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
''')
conn.commit()
conn.close()
print("✅ Database and table created.")
