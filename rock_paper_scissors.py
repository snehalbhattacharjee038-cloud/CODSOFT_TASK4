"""
Rock, Paper, Scissors
Play against the computer over multiple rounds with score tracking.
"""

import random

CHOICES = {"1": "rock", "2": "paper", "3": "scissors"}
SHORTCUTS = {"r": "rock", "p": "paper", "s": "scissors"}

# Each key beats its value
BEATS = {"rock": "scissors", "scissors": "paper", "paper": "rock"}

ART = {
    "rock": "[ ROCK ]",
    "paper": "[ PAPER ]",
    "scissors": "[ SCISSORS ]",
}


def get_user_choice():
    """Accept 1/2/3, r/p/s, or the full word. Returns None to quit."""
    while True:
        raw = input("Your choice (1-3, or q to quit): ").strip().lower()
        if raw in ("q", "quit"):
            return None
        if raw in CHOICES:
            return CHOICES[raw]
        if raw in SHORTCUTS:
            return SHORTCUTS[raw]
        if raw in BEATS:
            return raw
        print("  Invalid choice. Enter 1, 2, 3 (or r, p, s).")


def get_computer_choice():
    return random.choice(list(BEATS))


def decide_winner(user, computer):
    """Return 'user', 'computer' or 'tie'."""
    if user == computer:
        return "tie"
    return "user" if BEATS[user] == computer else "computer"


def show_instructions():
    print("=" * 40)
    print("      ROCK  -  PAPER  -  SCISSORS")
    print("=" * 40)
    print("Rules:")
    print("  Rock     beats Scissors")
    print("  Scissors beats Paper")
    print("  Paper    beats Rock")
    print("\nMenu:  1 = Rock   2 = Paper   3 = Scissors\n")


def show_scores(scores):
    print(f"\n  Score -> You: {scores['user']} | "
          f"Computer: {scores['computer']} | Ties: {scores['tie']}")


def play_round(scores):
    user = get_user_choice()
    if user is None:
        return False

    computer = get_computer_choice()
    print(f"\n  You chose:      {ART[user]}")
    print(f"  Computer chose: {ART[computer]}\n")

    winner = decide_winner(user, computer)
    scores[winner] += 1

    if winner == "tie":
        print("  It's a tie!")
    elif winner == "user":
        print(f"  You win! {user.title()} beats {computer}.")
    else:
        print(f"  You lose! {computer.title()} beats {user}.")

    show_scores(scores)
    return True


def final_summary(scores):
    rounds = sum(scores.values())
    print("\n" + "=" * 40)
    print(f"  Game over - {rounds} round(s) played")
    show_scores(scores)
    if scores["user"] > scores["computer"]:
        print("  Overall winner: YOU! Congratulations!")
    elif scores["user"] < scores["computer"]:
        print("  Overall winner: the Computer. Better luck next time!")
    elif rounds:
        print("  Overall result: a draw.")
    print("=" * 40)


def main():
    scores = {"user": 0, "computer": 0, "tie": 0}
    show_instructions()

    while True:
        if not play_round(scores):
            break
        again = input("\nPlay another round? (y/n): ").strip().lower()
        if again != "y":
            break
        print("\n" + "-" * 40)

    final_summary(scores)


if __name__ == "__main__":
    main()
