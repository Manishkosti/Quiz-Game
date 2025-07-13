<div align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=600&size=50&duration=4000&pause=1000&color=FFFFFF&background=000000&center=true&vCenter=true&width=800&height=100&lines=QUIZ-GAME" alt="Quiz-Game" />
  
  <div style="margin: 20px 0;">
    <img src="https://img.shields.io/github/stars/Manishkosti/Quiz-Game?style=for-the-badge&logo=github&logoColor=white&color=black&labelColor=black" alt="GitHub stars"/>
    <img src="https://img.shields.io/github/forks/Manishkosti/Quiz-Game?style=for-the-badge&logo=github&logoColor=white&color=black&labelColor=black" alt="GitHub forks"/>
    <img src="https://img.shields.io/github/issues/Manishkosti/Quiz-Game?style=for-the-badge&logo=github&logoColor=white&color=black&labelColor=black" alt="GitHub issues"/>
  </div>
  
  <p style="font-size: 18px; color: #666; font-weight: 500; margin: 20px 0;">
    A cross-platform Python quiz game that runs in the terminal. Supports multiple question types and tracks high scores.
  </p>
</div>

---


# 🚀 Quiz-Game

<div align="center">
  
  **Created by [Manishkosti](https://github.com/Manishkosti)**
  
  🗓️ **Created:** 7/13/2025 | 🔄 **Last Updated:** 7/13/2025
  
</div>

## 📖 About

Command-line Quiz Game is a terminal-based quiz application built with Python. It allows users to test their knowledge through a variety of question types — including multiple-choice, true/false, and open-ended — across different difficulty levels.

Designed for both fun and learning, the game includes sound effects, score tracking, and a persistent high-score leaderboard. It’s lightweight, easy to customize, and great for beginners looking to explore file handling, JSON parsing, and interactive CLI applications in Python.

Whether you're a student, teacher, or just a trivia enthusiast, this game provides an engaging way to challenge your brain!


## 🛠️ Tech Stack

<div align="left">
 Python 3.10+<br/>
 Standard libraries: json, time, os, pathlib<br/>
 Optional: winsound (Windows-only)
</div>


## 🎯 Getting Started

Clone this repo<br/>
Add your own questions in questions.json<br/>
Run: python quiz_game.py


## 🔧 Installation

```bash
# Clone the repository
git clone https://github.com/Manishkosti/Quiz-Game.git

# Navigate to project directory
cd Quiz-Game

# Make sure you have Python 3.10 or higher installed.

# Install dependencies
No external libraries required — the game uses only standard Python libraries.

# Start the development server
python quiz_game.py
```

## 🌟 Features

- 📚 Loads questions from JSON – Cleanly structured questions.json supports:
  - Multiple-choice
  - True/False
  - Open-ended
- 🎮 Interactive Game Loop – Play by difficulty level: Easy, Medium, or Hard
- 📊 Score Tracking – Keeps score per round, with a persistent high-score leaderboard
- 🔊 Cross-platform Sound Effects – Welcome, correct, and wrong answer tones using winsound (Windows fallback friendly)
- 💾 Persistent Data – High scores stored in high_scores.json
- ✨ Friendly UI – Styled CLI with feedback, retry prompts, and quit options

## 📚 Usage

After running the game with: python quiz_game.py
Follow the on-screen prompts:
1. Enter your name – Used to track high scores.
2. Choose a difficulty level:
   - 1 → Easy
   - 2 → Medium
   - 3 → Hard
3. Answer questions based on type:
   - ✅ Multiple Choice → Type the number of your chosen option
   - ✅ True/False → Type 1 for True or 2 for False (also accepts true, false, t, f)
   - ✅ Open-ended → Type your answer (not case-sensitive)
4. Get instant feedback:
   - ✔️ Correct answers earn 10 points
   - ❌ Wrong answers show the correct one
5. View your total score and the top 10 high scores
6. Choose to play another round or quit
   To quit at any time, just type: quit

---

<div align="center">
  <strong>⭐ Star this repository if you find it helpful!</strong>
  
  <br/>
  
  <a href="https://github.com/Manishkosti/Quiz-Game">
    <img src="https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github"   alt="View on GitHub"/>
  </a>
</div>
