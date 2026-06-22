# 🧮 CLI Calculator Project

A command-line based calculator built with Python that enables users to perform basic arithmetic operations interactively. The calculator supports continuous calculations, dynamic result updates, and a modular structure separating logic and visual components.

---

## 📌 Overview

The **CLI Calculator Project** is a terminal powered interactive calculator designed to execute basic mathematical operations such as addition, subtraction, multiplication, and division. Users can perform multiple calculations in a single session using an intuitive, prompt driven interface styled with ASCII art. The modular design and clean logic flow make this an excellent example of how to structure small yet scalable Python CLI projects.

---

## 🧠 Technologies and Concepts Used

- **Python 3** – The core language used for all logic and execution.
- **Function Mapping** – Arithmetic operations are stored in a dictionary with function references.
- **Modular Programming** – ASCII art is isolated into a separate module (`art.py`) for better readability and reusability.
- **Control Flow and Loops** – Enables decision making, recursion, and loop based session continuation.
- **Recursion** – Restarts the calculator session cleanly without global resets.
- **User Input Handling** – Dynamically responds to user decisions at each step.
- **CLI Aesthetics** – Uses ASCII art to enhance user experience visually.

---

## 🕹 Gameplay Mechanics

1. **Startup**:
   - The program begins by printing a calculator style ASCII logo.
   - Prompts the user to enter the first number.

2. **Operation Selection**:
   - Presents a list of available arithmetic operations (`+`, `-`, `*`, `/`).
   - Takes user input for the operation and the second number.

3. **Calculation and Continuation**:
   - Displays the result of the calculation.
   - Prompts the user:
     - `y`: Continue calculating with the result.
     - `n`: Start a fresh calculation from the beginning.

4. **Session Reset**:
   - If the user chooses to start over, the calculator clears the screen and restarts with a new first number.

---

## 📁 Project Structure

```text
cli-calculator-project/
    ├── calculator.py    # Main Python script with calculator logic
    ├── art.py           # Module containing ASCII art logo
    └── README.md        # Project documentation
```

---

### 🛠️ How to Run

> ⚠️ Make sure Python 3 is installed on your system.

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/Python-CLI-Project-Collection.git
   ```

2. **Navigate to the project folder**
   ```bash
   cd python-cli-project-collection/cli-python-mini-projects/cli-calculator-project
   ```

3. **Run the script**
   ```bash
   python calculator.py
   ```

---

### 📊 Sample Output

```text
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|

What is the first number?: 8
+
-
*
/
Pick an operation: *
What is the next number?: 3
8.0 * 3.0 = 24.0
Type 'y' to continue calculating with 24.0, or type 'n' to start a new calculation: y
+
-
*
/
Pick an operation: -
What is the next number?: 4
24.0 - 4.0 = 20.0
Type 'y' to continue calculating with 20.0, or type 'n' to start a new calculation: n

... (calculator resets)
```

---

## ✅ Key Takeaways

> 🚀 **Skills & Concepts Strengthened Through This Project**

### 🧠 Programming Logic & Problem Solving
- Crafted a modular and extensible calculator using pure Python logic without external libraries.
- Practiced the use of dictionaries to simulate a switch case operation which is a crucial pattern for real world applications.

### 🔄 Looping & State Management
- Leveraged `while` loops to continuously perform chained calculations.
- Implemented session resets using recursion, showcasing control flow mastery.

### 🧰 Functional Programming
- Applied clean and reusable functions for each arithmetic operation (add, subtract, multiply, divide).
- Enabled dynamic invocation of functions using symbolic input and function mapping.

### 💬 Interactive CLI Experience
- Designed a user friendly command-line interface with step by step guidance and real time feedback.
- Integrated ASCII art for branding and visual appeal using modular imports.

### 📐 Clean Code Principles
- Separated concerns by keeping UI (ASCII art) in a dedicated module (`art.py`).
- Maintained readability and structure using well named functions and variables.

### 🧪 Type Conversion & Data Handling
- Managed string to float conversions for user input while ensuring accurate calculations.
- Handled conditional logic for reusing previous results or starting fresh calculations.

---
