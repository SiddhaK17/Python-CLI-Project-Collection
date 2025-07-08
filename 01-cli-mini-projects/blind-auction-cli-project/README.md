# 🕶️ Blind Auction CLI Project

A command-line based anonymous bidding system built in Python. This project simulates a blind auction where participants place their bids without visibility into other bidders' offers. The program collects all bids and announces the highest bidder at the end, ensuring fairness and secrecy using basic control flow, dictionary operations, and clean I/O handling.

---

## 📝 Overview

The **Blind Auction CLI Project** is designed to demonstrate how a sealed bid auction can be executed via the terminal. Each participant provides their name and bid in a confidential manner. By simulating a screen clear after each bid, the program mimics the privacy of a real world blind auction. The highest bidder is calculated and declared once the bidding ends.

This project not only showcases user interaction in the CLI but also highlights the use of dictionaries, loops, functions, and simple data structures to build a real world solution with Python.

---

## 🛠️ Technologies and Concepts Used

- **Programming Language**: Python 3
- **Core Concepts**:
  - Functions and parameterized logic
  - Dictionary based data collection
  - Iteration and conditional statements
  - Terminal based user input/output
  - Modular design using ASCII art separation
  - Visual console clearing simulation (via `print("\n" * 20)`)

---

## 🎮 Gameplay Mechanics

1. Display a visually appealing auction logo using ASCII art.
2. Prompt the user to enter:
   - Their **name**
   - Their **bid amount**
3. Ask if there are more bidders:
   - If **yes**, simulate screen clearing for privacy and restart bidding input.
   - If **no**, process the final bids.
4. Determine the winner using a function that compares all recorded bids.
5. Display the winner’s name and bid amount.

---

## 📁 Project Structure

```
blind-auction-cli-project/
    ├── blind_auction.py       # Main auction logic and CLI interface
    ├── art.py                 # ASCII logo displayed at the start
    └── README.md              # Project documentation and usage guide
```

---

### 🛠️ How to Run

> ⚠️ Make sure Python 3 is installed on your system.

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/blind-auction-cli-project.git
   ```

2. **Navigate to the project folder**
   ```bash
   cd python-project-collection/01-cli-mini-projects/blind-auction-cli-project
   ```

3. **Run the script**
   ```bash
   python blind_auction.py
   ```

---

## 🧪 Sample Output

```
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\

What is your name?: Alice
What is your bid?: $150
Are there any other bidders? Type 'yes or 'no'.
yes


What is your name?: Bob
What is your bid?: $200
Are there any other bidders? Type 'yes or 'no'.
no

The winner is Bob with a bid of $200
```

---

## 💡 Key Takeaways

- Demonstrates practical application of **dictionaries** for user to value mapping.
- Reinforces use of **functions** for modular and reusable logic (e.g., finding highest bid).
- Teaches how to simulate **real-world interactions** using CLI tools and basic print based UI tricks.
- Great example of **user flow design**, making beginners think from a product user perspective.
- Ideal for strengthening **Python fundamentals** while solving a practical problem.

---