# 🃏 Blackjack CLI Game

> A sleek, interactive command-line Blackjack simulation, developed entirely in Python where players face off against a computer dealer, replicating classic casino logic and probability based decision making.

---

## 📘 Overview

The **Blackjack CLI Game** brings the core mechanics of casino style Blackjack to a terminal based environment, offering a text based gameplay experience powered by modular, reusable Python functions. Designed with real world Blackjack constraints, the game emulates an infinite card deck, dynamic Ace scoring, and automated dealer behavior.

This project demonstrates the practical implementation of game logic, state management, and decision structures, making it an excellent example of how to build scalable, logic driven CLI applications. The codebase is cleanly structured and ideal for further feature extensions like multiplayer, betting systems, or even transitioning to a GUI.

---

## 💻 Technologies & Concepts Used

- **Python 3.10+**
- **Functional Programming Principles**
- **Randomization Techniques (`random.choice`)**
- **Game State Management with Loops and Flags**
- **Control Flow & Decision Trees**
- **Data Structures: Lists, Conditionals**
- **ASCII Art for Visual Appeal**
- **Edge Case Logic (Blackjack, Dynamic Ace Handling, Bust)**

---

## 🕹️ Gameplay Mechanics

- ♠️ **Infinite Deck**: Cards are drawn from a virtual infinite deck; no duplicates or removals.
- ♥️ **Card Values**:
  - Number cards retain their face value.
  - Face cards (J, Q, K) count as `10`.
  - Aces count as `11` or `1` based on the player's hand.
- ♦️ **Player's Turn**:
  - Starts with two cards.
  - Chooses to either `Hit (y)` for another card or `Stand (n)` to stop.
- ♣️ **Dealer's Rule**:
  - Dealer draws cards until the total score is `17` or above.
- 🎯 **Winning Conditions**:
  - A score of `21` with two cards is a **Blackjack**.
  - Going over `21` results in a **bust**.
  - Final scores are compared to determine the winner.

---

## 📁 Project Structure

```
blackjack-project/
    ├── blackjack.py           # Main program with game loop and logic
    ├── art.py                 # ASCII banner for a fun visual introduction
    └── README.md              # Project documentation
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
   cd python-cli-project-collection/cli-python-mini-projects/blackjack-project
   ```

3. **Run the script**
   ```bash
   python blackjack.py
   ```

---

## 🧾 Sample Output

Do you want to play a game of Blackjack? Type 'y' or 'n': y


```
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           

Your cards: [10, 8], current score: 18
Computer's first card: 7
Type 'y' to get another card, type 'n' to pass: n

Your final hand: [10, 8], final score: 18
Computer's final hand: [7, 5, 9], final score: 21
You lose 😤

Do you want to play a game of Blackjack? Type 'y' or 'n': y



.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           

Your cards: [10, 11], current score: 21
Computer's first card: 10
Type 'y' to get another card, type 'n' to pass: n

Your final hand: [10, 11], final score: 21
Computer's final hand: [10, 10], final score: 20
You win 😃

Do you want to play a game of Blackjack? Type 'y' or 'n': n
```

---

## 🎯 Key Takeaways

> A showcase of clean code architecture, effective logic, and practical application of Python fundamentals all through a fun and classic game.

---

### ✅ Robust Game Logic  
Well aligned with traditional casino rules, this project handles core mechanics such as:

- Automatic Blackjack detection (`score == 0`)
- Dynamic Ace handling (switching between 11 and 1)
- Dealer drawing logic until reaching a score ≥ 17
- Bust scenarios for both player and dealer

---

### ✅ Clean Modular Architecture  
Each functionality is encapsulated in clear, purpose driven functions:

- `deal_card()` — Draws a random card  
- `calculate_score()` — Evaluates current hand with special case rules  
- `compare()` — Decides the outcome  
- `play_game()` — Controls game flow  

This structure promotes **reusability**, **testability**, and **ease of maintenance**.

---

### ✅ Enhanced User Interaction  
- Clear and contextual prompts throughout the game loop  
- Real time feedback on scores, decisions, and results  
- Visual clarity using ASCII art for branding and atmosphere

---

### ✅ Strategic Edge Case Handling  
Designed to gracefully handle special cases:

- Instant wins with Blackjack  
- Ace flexibility to prevent unintentional busts  
- Dealer's automated decision tree emulating realistic behavior

---

### ✅ Solid Grasp of Python Core Concepts  
Applies Python fundamentals proficiently:

- `random.choice()` for unpredictable gameplay  
- List manipulation and arithmetic evaluation  
- Control flow using `if-else`, `while`, and input based branching  
- Scoped, clean, and composable function definitions

---

### ✅ Foundations of CLI Game Development  
Demonstrates how to build engaging games purely within the terminal. No GUI, no frameworks... Just raw logic and decision making.

---

### ✅ Built for Extensibility  
This project is a perfect base for feature expansion. Potential upgrades include:

- 💰 **Betting System**  
- 🧑‍🤝‍🧑 **Multiplayer Support**  
- 🖥️ **GUI Integration** with `tkinter`, `PyQt`, or `Kivy`  
- 🧠 **AI Dealer Logic Enhancements**

---
