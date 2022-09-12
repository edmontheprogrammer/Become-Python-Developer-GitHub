# Create a number guessing game where the user enters a
# number and then tell the user if their guess is lower or higher
# Tell the user number of guess they took to get the number
import random
import time

print("Hi, Welcome to the guessing game. I am going to pick a number between 1 and 100.")
print("Please guess a number between 1 and 100")
time.sleep(3)
guess = int(input("What is your guess?: "))
correct_number = random.randint(1, 100)
time.sleep(2)

counter = 1
while guess != correct_number:
    time.sleep(1)
    counter += 1
    if guess < correct_number:
        guess = int(
            input("Wrong. You need to guess higher. What is your guess?: "))
    if guess > correct_number:
        guess = int(
            input("Wrong. You need to guess lower. What is your guess?: "))

print(
    f" The right answer was {correct_number} You got the right answer in {counter} tries. :)")
