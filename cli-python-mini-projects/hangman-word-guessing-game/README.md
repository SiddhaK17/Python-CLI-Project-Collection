# 🕹️ Hangman CLI Game

A command-line implementation of the classic Hangman game, built in Python. This project showcases control structures, modular code design, and basic ASCII rendering while delivering a fun, interactive user experience directly in the terminal.

---

## 🧠 Overview

This game challenges players to guess a hidden word one letter at a time. Each incorrect guess reduces the player's available lives and visually progresses the hangman drawing using ASCII art. The game ends when the player either successfully guesses the word or runs out of lives.

---

## ⚙️ Technologies & Concepts Used

- **Python 3.x**
- Modular Code Structure (`import`ed assets like ASCII art and word list)
- Lists, Conditionals, Loops
- User Input Handling
- Random Module for Word Selection
- ASCII Art Rendering
- Game State Management

---

## 🎮 Gameplay Mechanics

- The game selects a **random word** from a predefined list.
- Players are prompted to guess one letter at a time.
- Correct guesses update the display.
- Incorrect guesses decrease lives and advance the hangman drawing.
- The game ends when:
  - The player successfully guesses all letters.
  - The player runs out of lives (6 chances).
- Duplicate guesses are handled gracefully.

---

## 📁 Project Structure

```text
hangman-word-guessing-game/
    ├── hangman_game.py         # Main game logic
    ├── hangman_art.py          # Contains ASCII logo and hangman stages
    ├── hangman_words.py        # Contains the word list for the game
    └── README.md               # Project documentation
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
   cd python-cli-project-collection/cli-python-mini-projects/hangman-word-guessing-game
   ```

3. **Run the script**
   ```bash
   python hangman_game.py
   ```

---

### 📊 Sample Output

```text
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    

**************************** 6/6 LIVES LEFT ****************************
Guess a letter: m
You've chosen the correct letter!
Word to guess: m___
  +---+
  |   |
      |
      |
      |
      |
=========

**************************** 6/6 LIVES LEFT ****************************
Guess a letter: a
You've chosen the correct letter!
Word to guess: ma__
  +---+
  |   |
      |
      |
      |
      |
=========

**************************** 6/6 LIVES LEFT ****************************
Guess a letter: r
You've chosen the correct letter!
Word to guess: mar_
  +---+
  |   |
      |
      |
      |
      |
=========

**************************** 6/6 LIVES LEFT ****************************
Guess a letter: k
You've chosen the correct letter!
Word to guess: mark
  +---+
  |   |
      |
      |
      |
      |
=========

**************************** YOU WIN ****************************
```

---

## 🎯 Key Takeaways

- 🧩 **Problem-Solving Focus**: Strengthens logical thinking and control flow management through an engaging and classic game scenario.
- 🧠 **Concept Mastery**: Reinforces core Python concepts such as:
  - Loops and conditionals
  - List and string manipulation
  - Modular programming (via multiple Python files)
  - User input validation and edge case handling
- 🖼️ **Terminal UI Design**: Introduces ASCII-based UI rendering for a visual representation of the game’s state, enhancing the user experience without external libraries.
- 📁 **Modular Architecture**: Separates responsibilities into individual files (`art`, `word list`, `logic`) — making the project clean, readable, and maintainable.
- 🔁 **Replayability Potential**: Lays a solid foundation for enhancements such as difficulty levels, leaderboard tracking, or graphical interfaces using Tkinter or web frameworks.

---