from flask import Flask, request, jsonify
import sqlite3
import pandas as pd
import os

app = Flask(__name__)
DATABASE = 'accredited_staff.db'

def setup_database():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS staff (
                    id TEXT PRIMARY KEY,
                    sp_number TEXT UNIQUE,
                    name TEXT,
                    verified INTEGER DEFAULT 0
                 )''')
    conn.commit()
    conn.close()

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    if file:
        file.save(file.filename)
        update_database(file.filename)
        os.remove(file.filename)
        return jsonify({"message": "File uploaded and database updated successfully"}), 200

@app.route('/verify', methods=['POST'])
def verify_staff():
    data = request.get_json()
    barcode_id = data.get('barcode_id')
    if not barcode_id:
        return jsonify({"error": "No barcode ID provided"}), 400
    
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('SELECT name, sp_number, verified FROM staff WHERE id = ?', (barcode_id,))
    result = c.fetchone()
    if result:
        name, sp_number, verified = result
        if verified == 0:  # Not verified yet
            c.execute('UPDATE staff SET verified = 1 WHERE id = ?', (barcode_id,))
            conn.commit()
            conn.close()
            return jsonify({"verified": True, "name": name, "sp_number": sp_number, "message": "Verification successful"}), 200
        else:
            conn.close()
            return jsonify({"verified": False, "name": name, "sp_number": sp_number, "message": "Already verified"}), 400
    else:
        conn.close()
        return jsonify({"verified": False, "message": "Not found"}), 404

def update_database(filename):
    df = pd.read_excel(filename)
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    for index, row in df.iterrows():
        c.execute('INSERT OR IGNORE INTO staff (id, sp_number, name) VALUES (?, ?, ?)', (row['ID'], row['SPNumber'], row['Name']))
    conn.commit()
    conn.close()

if __name__ == '__main__':
    setup_database()
    app.run(host='0.0.0.0', port=5000, debug=True)
