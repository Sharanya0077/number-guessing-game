cat <<'EOF' > README.md
# 🎯 Number Guessing Game

A simple Python game where the computer generates a random number and the player has to guess it.  
After every guess, the game gives a hint — **“Higher”** or **“Lower”** — to help the player reach the correct answer.  
The game also tracks the number of attempts used.

## 🕹️ Gameplay Rules
- The computer randomly chooses a number within a fixed range (e.g., **1 to 100**)
- If your guess is **too high** → **Lower please**
- If your guess is **too low** → **Higher please**
- The game ends when:
  - ✅ You guess the number
  - ❌ Or you exceed the maximum attempts (e.g., **10 attempts**)

## ⚙️ How to Run
```bash
python number_guessing_game.py
