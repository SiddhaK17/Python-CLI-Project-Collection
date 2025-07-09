# 🪨 Rock Paper Scissors – A Command Line Game in Python

A clean and interactive implementation of the classic **Rock, Paper, Scissors** game using Python.  
This CLI-based project allows the user to play against the computer in a one-round match with visually styled ASCII output.

---

## 📌 Overview

This project demonstrates the fundamentals of **control flow**, **user input handling**, and **randomized logic** using Python.  
It's part of a broader collection of CLI mini-projects built to strengthen core Python programming concepts.

---

## ⚙️ Technologies & Concepts

- **Python 3.x**
- `random` module for generating non-deterministic computer moves
- ASCII art to enhance user experience
- Input validation and error handling
- Conditional logic for game result computation

---

## 🧠 Gameplay Mechanics

- The user is prompted to select:
  - `0` for Rock
  - `1` for Paper
  - `2` for Scissors

- The computer randomly selects its move.

- The winner is determined using traditional Rock-Paper-Scissors rules:
  - Rock beats Scissors
  - Scissors beats Paper
  - Paper beats Rock

- The game outputs:
  - User's choice with ASCII art
  - Computer's choice with ASCII art
  - Final result: **Win**, **Lose**, or **Draw**

---

## 📂 Project Structure

```plaintext
cli-python-mini-projects/
└── rock-paper-scissors/
    ├── rock_paper_scissors.py   # Main executable Python script
    └── README.md                # Project documentation
```

---

### 🛠️ How to Run

> ⚠️ Make sure Python 3 is installed on your system.

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/python-cli-project-collection.git
   ```

2. **Navigate to the project folder**
   ```bash
   cd python-cli-project-collection/cli-python-mini-projects/rock-paper-scissors
   ```

3. **Run the script**
   ```bash
   python rock_paper_scissors.py
   ```

---

## 🖼 Sample Output

```text
What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.
> 1

    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

Computer chose:

    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

You Win!
```
---

### ✅ Key Takeaways

- 🚀 **Hands-on understanding of conditional logic** in Python (`if`, `elif`, `else`).
- 🧠 Learned how to implement **basic game mechanics** through user input and computer-generated outcomes.
- 🎲 Applied **Python’s `random` module** to simulate unpredictable computer decisions.
- 🖼️ Practiced the use of **multi-line ASCII art** for creating a visually interactive CLI experience.
- 🔁 Improved understanding of **input validation** by handling out-of-bound values gracefully.
- 🧱 Gained foundational experience with:
  - List indexing and control structures.
  - Clean, readable CLI outputs with structured results.
- 🧪 Reinforced the habit of **testing each outcome path** to ensure a complete game cycle.

---