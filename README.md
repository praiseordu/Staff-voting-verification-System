# Staff-voting-verification-System
A Voting Verification system. This use case is for the Federal University of Technology Owerri

This project is a Staff Verification System for the Federal University of Technology, Owerri. It consists of a Flask server and a Tkinter-based GUI for verifying staff members.

## Features
- Upload Excel file with staff details.
- Verify staff using a barcode ID.
- Display verification results with a unique voting code.

## Requirements
- Python 3.x
- Flask
- pandas
- openpyxl
- requests
- tkinter

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/praiseordu/Staff-voting-verification-System.git
   cd staff-verification-system
Install the dependencies

It's recommended to use a virtual environment. You can set one up using venv:

bash

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install the required packages:

bash

pip install -r requirements.txt

Run the Flask server

bash

python app.py

Run the Tkinter GUI

bash

cd frontend
python main.py

Usage

    Use the "Upload Excel" button in the GUI to upload a file with staff details.
    Enter a barcode ID and click "Verify" to verify a staff member.
    The verification result will display the staff name, SP number, and a unique voting code if the verification is successful.

Project Structure

perl

staff-verification-system/
├── app.py                     # Contains the Flask server code
├── frontend/
│   ├── main.py                # Contains the Tkinter GUI code
│   ├── logo.png               # Logo image used in the GUI
├── requirements.txt           # Contains the project dependencies
├── README.md                  # Project description and instructions
└── .gitignore                 # Specifies files and directories to ignore

.gitignore

markdown

__pycache__/
*.pyc
*.pyo
*.pyd
.DS_Store
*.db
venv/

License

This project is licensed under the GNU General Public License v3.0. See the LICENSE file for details.
Contact

If you have any questions or suggestions, feel free to contact me at [praiseordu@gmail.com].
Acknowledgements

    Federal University of Technology, Owerri for providing the use case.
    The developers and maintainers of the libraries used in this project.
