import random

lowest_number = 1
highest_number = 10
random_number = random.randint(lowest_number,highest_number)
guesses = 0
is_playing = True

print("Welcome to Number Guessing Game")
print(f"Select a number between {lowest_number} to {highest_number}")

while is_playing:
  guess = input("Enter your guess: ")

  if guess.isdigit():
    guess = int(guess)
    if guess < 1 or guess > 10:
      print("You have entered a wrong number")
      print(f"Select a number between {lowest_number} to {highest_number}")
    elif guess > random_number:
      guesses += 1
      print("You are too close!")
      print("You have choosen higher number")
    elif guess < random_number:
      guesses += 1
      print("You are too close!")
      print("You have choosen lower number")
    else:
      guesses += 1
      print(f"Congratulation! You have choosen {guess}  the right one")
      print(f"You have tried {guesses} times and won")
      is_playing = False
  else:
    print("Invalid input")
    print(f"Select a number between {lowest_number} to {highest_number}")
     