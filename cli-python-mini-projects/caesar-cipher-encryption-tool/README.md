# 🔐 Caesar Cipher – Text Encryption & Decryption CLI Program

A streamlined command-line tool that demonstrates the classical Caesar Cipher encryption technique allowing users to securely encode or decode text using a specified shift value. Designed for simplicity and clarity, this project provides an excellent introduction to cryptographic logic and user interactive Python applications.

---

## 📖 Overview

The **Caesar Cipher** is a fundamental encryption method where each letter in the plaintext is shifted a fixed number of positions down or up the alphabet. This Python implementation provides a fully functional, user friendly interface to explore both encryption and decryption processes using this symmetric substitution cipher.

Whether you're a beginner learning about ciphers or a developer building foundational CLI tools, this project exemplifies clean coding principles, input validation, and logical structuring in Python.

---

## 🛠️ Technologies & Concepts Used

- **Python 3.x** – Core programming language used for logic and CLI interactions  
- **ASCII Art** – Enhances UX with stylized banner displays  
- **List Manipulation** – Efficient handling of character shifting and wrapping  
- **Modular Programming** – Separation of logic and visual components  
- **Control Flow** – Use of loops, conditionals, and error handling  
- **Symmetric Encryption Logic** – Implements classical Caesar Cipher technique  
- **Robust Input Validation** – Ensures smooth user interaction with fallback mechanisms  

---

## ⚙️ Program Logic & Flow

1. Displays a branded ASCII logo upon launch for branding and clarity.
2. Asks the user to choose between `encode` (encrypt) and `decode` (decrypt).
3. Prompts for a message and a numeric shift value.
4. Applies the Caesar Cipher logic while preserving non alphabet characters.
5. Outputs the resulting encoded or decoded message.
6. Offers the option to restart or exit the application.
7. Handles invalid inputs with custom error messages to enhance user experience.

---

## 📁 Project Structure

```text
caesar-cipher-encryption-tool/
    ├── caesar_cipher.py   # Main Caesar Cipher encryption/decryption logic
    ├── art.py             # ASCII art/logo used in the program
    └── README.md          # Documentation for the project
```

### 🛠️ How to Run

> ⚠️ Make sure Python 3 is installed on your system.

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/Python-CLI-Project-Collection.git
   ```

2. **Navigate to the project folder**
   ```bash
   cd python-cli-project-collection/cli-python-mini-projects/caesar-cipher-encryption-tool
   ```

3. **Run the script**
   ```bash
   python caesar_cipher.py
   ```

---

### 📊 Sample Output

```text
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           

Type 'encode' to encrypt, type 'decode' to decrypt:
> encode
Type your message:
> hello world!
Type the shift number:
> 5
Here is the encoded result: mjqqt btwqi!

Type 'yes' if you want to go again. Otherwise, type 'no':
> yes

 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           

Type 'encode' to encrypt, type 'decode' to decrypt:
> decode
Type your message:
> mjqqt btwqi!
Type the shift number:
> 5
Here is the decoded result: hello world!

Type 'yes' if you want to go again. Otherwise, type 'no':
> no
Thankyou for using Caesar Cipher. Goodbye!
```

---

## 🚀 Key Takeaways

- 📚 **Applied Cryptography Basics**: Successfully implemented a classical Caesar Cipher algorithm, reinforcing foundational knowledge in symmetric encryption.

- 💡 **Clean CLI Design**: Designed a user friendly command line interface that ensures intuitive interactions and real time feedback.

- 🔁 **Modular Code Structure**: Separated logic from visual presentation (ASCII art) for better readability, scalability, and maintenance.

- 🧠 **Enhanced Input Handling**: Introduced robust validation to gracefully handle unexpected or invalid user inputs, improving overall UX.

- 🔄 **Reusable Function Design**: Built a flexible `caesar()` function that efficiently handles both encoding and decoding with minimal changes.

- 🧪 **Practical Application of Python Fundamentals**: Strengthened core Python skills including loops, conditionals, string operations, and list indexing.

- 🎨 **Engaging User Experience**: Elevated engagement using ASCII art branding and dynamic prompts that make encryption feel interactive and fun.

---
