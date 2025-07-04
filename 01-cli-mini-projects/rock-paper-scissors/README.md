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
01-cli-mini-projects/
└── rock-paper-scissors/
    ├── rock_paper_scissors.py   # Main executable Python script
    └── README.md                # Project documentation
```

---

## 🚀 How to Run

> Make sure Python 3 is installed on your system.

1. Clone this repository or download the folder manually.

2. Open a terminal and navigate to the project directory:
   ```bash
   cd path/to/rock-paper-scissors

3. Run the program:
   python rock_paper_scissors.py

- If you're on macOS/Linux, you may need to use python3 instead.

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