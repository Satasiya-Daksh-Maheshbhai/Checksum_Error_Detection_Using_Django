# 📡 Error Detection Using Checksum
# 📌 Project Overview

This project is a web-based Error Detection System developed using Django (Python).
It demonstrates how the Checksum method is used to detect transmission errors in digital data communication.

The system allows users to enter binary data and performs checksum calculation step-by-step. It also verifies whether the received data contains an error or not.

# 🎯 Objective

To implement the Checksum Error Detection Technique

To show step-by-step binary addition

To generate 1's complement checksum

To verify whether transmitted data is error-free

# ⚙️ Technologies Used

Python

Django

HTML

CSS

Bootstrap (for styling)

# 🚀 Features

Accepts binary input from user

Performs binary addition vertically

Shows intermediate addition steps

Generates final checksum using 1’s complement

Validates received data

Displays whether data is Error-Free or Error Detected

# 🧮 Working of Checksum

User enters binary data blocks (example: 1011 1001 1100)

System adds all blocks using binary addition

If carry is generated, it is added back (end-around carry)

Final sum is generated

1’s complement of the sum is calculated

That result becomes the Checksum

During verification:

If final result contains all 0’s → No Error

Otherwise → Error Detected

# 📂 Project Structure

views.py → Contains checksum logic

urls.py → URL routing

templates/ → HTML pages

manage.py → Django project manager

# ▶️ How to Run the Project (Without Virtual Environment)

Install Python (3.x)

Install Django

pip install django


Clone the repository

git clone https://github.com/Satasiya-Daksh-Maheshbhai/Checksum_Error_Detection_Using_Django.git


Run migrations

python manage.py migrate


Start server

python manage.py runserver


Open browser

http://127.0.0.1:8000/

📊 Example Input & Output

Input:

1011
1001
1100


Output:

Binary Addition (Step-by-step)

Final Sum

1’s Complement

Generated Checksum

Error Status

# 📚 Applications

Computer Networks

Data Communication Systems

Error Detection in Digital Transmission

Educational Demonstration Tool

# 🏁 Conclusion

This project demonstrates how the Checksum technique is used in real-world communication systems to detect transmission errors.
It provides a clear visualization of binary addition and 1’s complement calculation, making it useful for learning and practical understanding of error detection methods.

# Sample Output :
<img width="1035" height="878" alt="image" src="https://github.com/user-attachments/assets/dfd0b506-f1a3-43f8-804c-b6fb4c9b078b" />
<img width="975" height="896" alt="image" src="https://github.com/user-attachments/assets/4b5c2102-e8df-461f-ae7f-6c6dfae5629b" />
