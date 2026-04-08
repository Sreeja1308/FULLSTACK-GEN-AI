import random

choices = ["rock", "paper", "scissors"]
user_history = {"rock": 0, "paper": 0, "scissors": 0}

def predict_user_move():
    if all(v == 0 for v in user_history.values()):
        return random.choice(choices)  # no data yet

    # Predict the most frequent user move
    most_frequent = max(user_history, key=user_history.get)

    # Return what beats the most frequent move
    if most_frequent == "rock":
        return "paper"
    elif most_frequent == "paper":
        return "scissors"
    else:
        return "rock"

while True:
    user = input("Enter Rock, Paper, or Scissors (or Q to quit): ").lower()
    if user == 'q':
        print("Thanks for playing!")
        break
    if user not in choices:
        print("Invalid input. Try again.")
        continue

    user_history[user] += 1
    ai = predict_user_move()

    print(f"AI chose: {ai}")

    if user == ai:
        print("It's a tie!")
    elif (user == "rock" and ai == "scissors") or \
         (user == "paper" and ai == "rock") or \
         (user == "scissors" and ai == "paper"):
        print("You win!")
    else:
        print("AI wins!")
