"""
Command‑line Quiz Game
──────────────────────
• Reads questions from questions.json
• Supports multiple‑choice, true/false & open‑ended
• Tracks scores, high‑scores, rounds and difficulty
"""

from pathlib import Path
import json, time, os
from sounds import play_welcome_sound, play_correct_sound, play_wrong_sound

QUESTIONS_FILE = "questions.json"
HIGH_SCORES_FILE = "high_scores.json"

# ────────────────────────────────
#  Utility helpers
# ────────────────────────────────
def load_questions(path: str) -> list[dict]:
    try:
        with open(path, encoding="utf‑8") as f:
            data = json.load(f)["questions"]
    except (FileNotFoundError, KeyError, json.JSONDecodeError):
        print(f"❌  Couldn’t load {path}")
        return []
    return data


def ask_yes_no(prompt: str) -> bool:
    while (choice := input(f"{prompt} (y/n) ➜ ").strip().lower()) not in ("y", "n", "yes", "no"):
        print("Type y or n.")
    return choice.startswith("y")


def select_difficulty() -> str:
    mapping = {"1": "easy", "2": "medium", "3": "hard"}
    print("\nDifficulty:\n 1. Easy\n 2. Medium\n 3. Hard")
    while (pick := input("Choose (1/2/3) ➜ ").strip()) not in mapping:
        print("Please enter 1, 2 or 3.")
    return mapping[pick]


# ────────────────────────────────
#  I/O
# ────────────────────────────────
def display_welcome() -> str:
    play_welcome_sound()
    print("\n" * 40)
    print("*" * 60)
    print("*{:^58s}*".format("WELCOME TO THE QUIZ GAME"))
    print("*" * 60, "\n")
    name = input("Your name ➜ ").strip() or "Player"
    print(f"\nWelcome, {name}!")
    time.sleep(1)
    return name


def show_question(q: dict) -> str | None:
    print("\n" + "-" * 60)
    print("Q:", q["question"])
    q_type = q["type"]

    if q_type == "multiple-choice":
        for idx, opt in enumerate(q["options"], 1):
            print(f"  {idx}. {opt}")
        valid = [str(i) for i in range(1, len(q["options"]) + 1)]

    elif q_type == "true/false":
        print("  1. True\n  2. False")
        valid = ["1", "2", "true", "false", "t", "f"]

    else:  # open‑ended
        valid = None

    while True:
        raw = input("Your answer ➜ ").strip().lower()
        if raw == "quit":
            return None
        if valid is None or raw in valid:
            return raw
        print("Invalid. Try again or type 'quit'.")


def is_correct(q: dict, ans: str) -> bool:
    if q["type"] == "multiple-choice":
        return int(ans) - 1 == q["answer"]
    if q["type"] == "true/false":
        return (ans[0] == 't') == (str(q["answer"]).lower()[0] == 't')
    return ans.lower() == str(q["answer"]).lower()


# ────────────────────────────────
#  High‑scores
# ────────────────────────────────
def load_scores() -> list[dict]:
    if Path(HIGH_SCORES_FILE).exists():
        with open(HIGH_SCORES_FILE, encoding="utf‑8") as f:
            return json.load(f)
    return []


def save_score(name: str, score: int):
    scores = load_scores()
    scores.append({"name": name, "score": score})
    scores.sort(key=lambda x: x["score"], reverse=True)
    with open(HIGH_SCORES_FILE, "w", encoding="utf‑8") as f:
        json.dump(scores[:10], f, indent=2)


def show_scores():
    scores = load_scores()
    if not scores:
        print("No high‑scores yet.")
        return
    print("\n── High Scores ──")
    for i, s in enumerate(scores, 1):
        print(f"{i:2d}. {s['name']:<15} {s['score']}")


# ────────────────────────────────
#  Game loop
# ────────────────────────────────
def run_quiz(questions: list[dict]):
    name = display_welcome()
    while True:
        diff = select_difficulty()
        round_qs = [q for q in questions if q["difficulty"] == diff]
        score = 0

        for q in round_qs:
            ui = show_question(q)
            if ui is None:
                print("\n👋  Bye!")
                return
            correct = is_correct(q, ui)
            if correct:
                play_correct_sound()
                score += 10
                print("✅  Correct!")
            else:
                play_wrong_sound()
                print(f"❌  Wrong. Ans: {q['answer']}")

        print("\n" + "=" * 60)
        print(f"{name}, your score: {score}/{len(round_qs)*10}")
        save_score(name, score)
        show_scores()
        print("=" * 60)

        if not ask_yes_no("Play another round?"):
            break
    print("\nThanks for playing, {}! 👋".format(name))


# ────────────────────────────────
if __name__ == "__main__":
    if Path(QUESTIONS_FILE).exists():
        run_quiz(load_questions(QUESTIONS_FILE))
    else:
        print(f"{QUESTIONS_FILE} not found.")