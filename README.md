# 🎯 Python Number Guessing Game

A simple terminal-based **Number Guessing Game** written in Python.

The game randomly generates a number, and your goal is to guess it before you run out of attempts. It includes multiple difficulty levels, a fully customizable mode, and input validation to prevent invalid values.

---

## ✨ Features

* 🎲 Random number generation
* 📈 Five built-in difficulty levels
* ⚙️ Custom difficulty mode
* ✅ Input validation
* 🔁 Play again option
* 🚪 Quit anytime from the main menu
* 📝 Keeps track of previous guesses internally

---

## 📋 Difficulty Levels

| Difficulty     | Number Range |    Attempts |
| -------------- | -----------: | ----------: |
| Easy           |      1 - 100 |          10 |
| Medium         |      1 - 100 |           5 |
| Medium-Hard    |     1 - 1000 |           5 |
| Hard           |     1 - 1000 |           3 |
| Extremely Hard |     1 - 1000 |           1 |
| Custom         |  Your choice | Your choice |

---

## 🛠️ Requirements

* Python 3.x

No external libraries are required. The game only uses Python's built-in `random` module.

---

## ▶️ How to Run

1. Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
```

2. Open the project folder:

```bash
cd YOUR_REPOSITORY
```

3. Run the program:

```bash
python main.py
```

> Replace `main.py` with your Python file's name if it is different.

---

## 🎮 How to Play

1. Launch the game.
2. Choose one of the available difficulty levels:

   * **E** – Easy
   * **M** – Medium
   * **MH** – Medium-Hard
   * **H** – Hard
   * **X** – Extremely Hard
   * **C** – Custom
   * **Q** – Quit
3. Enter your guesses.
4. The game will tell you whether your guess is too high or too low.
5. Guess the correct number before you run out of attempts.
6. Choose whether you want to play another round.

---

## ⚙️ Custom Mode Rules

When creating a custom game:

* Numbers must be integers.
* Numbers cannot be negative.
* The lowest number must be smaller than the highest number.
* The lowest and highest numbers cannot be the same.

If any rule is broken, the game asks you to enter the values again.

---

## 📂 Project Structure

```
.
├── main.py
└── README.md
```

---

## 💡 Future Improvements

Some ideas for future updates:

* Save high scores
* Display all guessed numbers after the game
* Hint system (warmer/colder)
* Multiple game modes
* Score system
* Difficulty based on percentages
* GUI version using Tkinter or Pygame
* Multiplayer mode
* Statistics (wins, losses, average guesses)

---

## 📜 License

This project is open source. Feel free to use, modify, and improve it for learning purposes.

---

## 👨‍💻 Author

Created by **Mirshad Rahman**.

If you enjoyed this project, consider giving the repository a ⭐!
