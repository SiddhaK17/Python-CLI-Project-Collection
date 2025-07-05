# 🔐 Secure Password Generator (CLI-Based)

A robust, customizable password generator built in Python. This command-line tool allows users to create secure passwords based on preferred character types — letters, symbols, and numbers with randomized output for enhanced strength and privacy. Ideal for both learners and developers seeking local, dependency free security tools.

---

### 🧾 Overview

This is a command-line based **Secure Password Generator** developed in Python. The program enables users to generate strong, randomized passwords by specifying the number of **letters**, **symbols**, and **numbers** they want to include. It ensures a high degree of password entropy by shuffling the character sequence, making the password resilient against pattern based attacks.

This project demonstrates fundamental Python programming concepts while offering practical functionality for real world use.

---

### 🧰 Technologies & Concepts Used

- **Python 3.x**
- Standard Library:
  - `random` — for character selection and shuffling
- Programming Constructs:
  - Lists and list operations
  - User input handling via `input()`
  - `for` loops and range iteration
  - String concatenation
  - CLI-based interaction

  ---

### 🎮 Program Logic & Flow

1. **User Prompting**  
   The program requests the user to input:
   - Number of **letters**
   - Number of **symbols**
   - Number of **numbers**

2. **Character Pooling**  
   Based on the inputs:
   - Random characters are selected from pre defined lists.
   - All chosen characters are stored in a master list (`password_list`).

3. **Shuffling for Randomness**  
   The collected characters are **shuffled** using `random.shuffle()` to ensure unpredictability.

4. **Password Assembly**  
   The final password is constructed by concatenating the shuffled characters.

---

### 📂 Project Structure

```plaintext
01-cli-mini-projects/
└── secure-password-generator/
    ├── secure_password_generator.py   # Main executable Python script
    └── README.md                      # Project documentation
```

---

### 🛠️ How to Run

> ⚠️ Make sure Python 3 is installed on your system.

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/python-project-collection.git
   ```

2. **Navigate to the project folder**
   ```bash
   cd python-project-collection/01-cli-mini-projects/secure-password-generator
   ```

3. **Run the script**
   ```bash
   python secure_password_generator.py
   ```

---

### 📊 Sample Output

```text
Welcome to the PyPassword Generator!
How many letters would you like in your password?
> 5
How many symbols would you like?
> 3
How many numbers would you like?
> 2

Password list before shuffling : ['g', 'A', 'r', 'm', 'T', '&', '#', ')', '4', '2']
Password list after shuffling  : ['#', '4', '&', 'r', ')', '2', 'g', 'A', 'T', 'm']
Your password is: #4&r)2gATm
```

---

### ✅ Key Benefits

- **Customizable:** Define your own password structure  
- **Secure:** High randomness using true shuffling  
- **No Dependencies:** Fully offline, runs on any machine with Python 3  

---