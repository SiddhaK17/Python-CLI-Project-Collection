# ☕ Coffee Machine Simulator (CLI Project)

A terminal-based Python program that simulates a real world coffee vending machine. Users can purchase different types of coffee, manage resources, process coin based payments, and monitor transaction reports — all via an interactive command line interface.

---

## 🧩 Overview

This project is an intermediate level CLI based Python application that mimics the behavior of a coffee vending machine. It allows users to order coffee (espresso, latte, or cappuccino), processes virtual coins as payment, manages machine resources (water, milk, coffee), and prints reports. It was built as part of my Python learning journey to practice control flow, functions, loops, dictionaries, and conditional logic in a real world inspired mini project.

---

## 🧪 Technologies and Concepts Used

- **Python 3**
- **Command-Line Interface (CLI) Interaction**
- **Functional Programming**
- **Conditional Logic and Control Flow**
- **Loops (while and for)**
- **Dictionaries for Nested Data Structures**
- **Global Variables and State Management**
- **String Interpolation and Formatting**
- **Basic Arithmetic and Rounding**
- **User Input Validation**

---

## 🎮 Gameplay Mechanics / Features

- ☕ **Coffee Menu Display**: Shows available coffee options and their prices upon program start.
- 🧾 **Order Handling**: Users can choose from espresso, latte, or cappuccino.
- 💰 **Coin Processing**: Simulates real world coin insertion (quarters, dimes, nickels, pennies).
- 🧮 **Transaction Validation**: Checks if sufficient payment was made, calculates and returns change.
- 🧯 **Resource Management**: Validates ingredient availability and deducts used resources.
- 📊 **Live Reporting**: Users can view current inventory and profit via the `report` command.
- 🔌 **Shutdown Feature**: Type `off` to safely power off the machine.

---

## 📁 Project Structure

```
coffee-machine-simulator-cli/
    ├── main.py        # Main script containing the game logic
    └── README.md      # Project documentation
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
   cd python-cli-project-collection/cli-python-mini-projects/coffee-machine-simulator-cli
   ```

3. **Run the script**
   ```bash
   python main.py
   ```

---

## 📌 Sample Output

```
☕ Welcome to the Python Coffee Machine ☕

Here are our coffee options and their prices:
→ Espresso: $1.5
→ Latte: $2.5
→ Cappuccino: $3.0

What would you like? (espresso/latte/cappuccino): latte
Please insert coins.
how many quarters?: 10
how many dimes?: 0
how many nickles?: 0
how many pennies?: 0
Here is $0.0 in change.
Here is your latte ☕️. Enjoy!

What would you like? (espresso/latte/cappuccino): report
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5

What would you like? (espresso/latte/cappuccino): espresso
Please insert coins.
how many quarters?: 6
how many dimes?: 0
how many nickles?: 0
how many pennies?: 0
Here is $0.0 in change.
Here is your espresso ☕️. Enjoy!

What would you like? (espresso/latte/cappuccino): cappuccino
Sorry there is not enough milk.

What would you like? (espresso/latte/cappuccino): off
```

---

## ✨ Key Highlights

- 🧠 **Interactive Console Experience**: Simulates a real world coffee vending machine experience directly within the terminal.
  
- 💰 **Coin-Based Payment System**: Accepts user input for different coin denominations (quarters, dimes, nickels, pennies) and calculates the total inserted value.

- 🚰 **Resource Management**: Tracks and updates ingredient availability (water, milk, coffee) after each transaction.

- ✅ **Transaction Validation**: Ensures sufficient resources and payment before dispensing coffee. Automatically handles change or refunds for insufficient funds.

- 🧾 **Dynamic Reporting**: Users can type `report` anytime to get real-time insights into remaining ingredients and accumulated profit.

- 📋 **Clean and Modular Codebase**: Built with modular functions (`is_resource_sufficient()`, `process_coins()`, `make_coffee()`, etc.) that enhance code readability and maintainability.

- 📈 **Scalable Logic**: Easily extendable to include more drinks, currencies, or additional features like user profiles or usage logs.

- 💬 **User-Friendly Prompts**: Provides clear guidance and feedback messages for all interactions to ensure a smooth user experience.

---
