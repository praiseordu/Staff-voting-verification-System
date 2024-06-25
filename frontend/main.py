import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import PhotoImage
import requests
import uuid
import os

SERVER_IP = '172.16.0.137'

def generate_voting_code():
    return str(uuid.uuid4())

def upload_excel():
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx;*.xls")])
    if file_path:
        with open(file_path, 'rb') as f:
            response = requests.post(f'http://{SERVER_IP}:5000/upload', files={'file': f})
        if response.status_code == 200:
            messagebox.showinfo("Success", "File uploaded and database updated successfully")
        else:
            messagebox.showerror("Error", "Failed to upload file")

def verify(event=None):
    barcode_id = barcode_entry.get()
    response = requests.post(f'http://{SERVER_IP}:5000/verify', json={'barcode_id': barcode_id})
    if response.status_code == 200:
        data = response.json()
        if data['verified']:
            voting_code = generate_voting_code()
            result_label.config(
                text=f"Verified: {data['name']} (SP Number: {data['sp_number']})\nVoting Code: {voting_code}", 
                fg='green', 
                font=("Helvetica", 34, "bold")
            )
        else:
            result_label.config(
                text=f"Already Verified: {data['name']} (SP Number: {data['sp_number']})", 
                fg='red', 
                font=("Helvetica", 34, "bold")
            )
    elif response.status_code == 404:
        result_label.config(
            text="Not Found", 
            fg='red', 
            font=("Helvetica", 34, "bold")
        )
    else:
        result_label.config(text=response.json().get('message', 'Verification failed'))
    barcode_entry.delete(0, tk.END)

base_dir = os.path.dirname(os.path.abspath(__file__))
logo_path = os.path.join(base_dir, 'logo.png')

root = tk.Tk()
root.title("Staff Verification System")

logo_image = PhotoImage(file=logo_path)

header_frame = tk.Frame(root)
header_frame.pack(pady=10)

logo_label = tk.Label(header_frame, image=logo_image)
logo_label.pack(side="left")

title_label = tk.Label(
    header_frame, 
    text="Federal University of Technology, Owerri\nStaff Verification System", 
    font=("Helvetica", 16, "bold"),
    justify="left"
)
title_label.pack(side="left", padx=10)

tk.Label(root, text="Enter Barcode ID:", font=("Helvetica", 12)).pack(pady=5)
barcode_entry = tk.Entry(root, font=("Helvetica", 12))
barcode_entry.pack(pady=5)
barcode_entry.focus_set()

barcode_entry.bind('<Return>', verify)

verify_button = tk.Button(root, text="Verify", command=verify, font=("Helvetica", 12))
verify_button.pack(pady=5)

upload_button = tk.Button(root, text="Upload Excel", command=upload_excel, font=("Helvetica", 12))
upload_button.pack(pady=5)

result_label = tk.Label(root, text="", font=("Helvetica", 34,"bold"))
result_label.pack(pady=5)

root.mainloop()
