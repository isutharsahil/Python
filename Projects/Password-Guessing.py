import random

easy = ["apple","train","tiger","monkey","money"]
medium = ["judge", "style", "ghost", "query", "rhyme"]
hard = ["fordmustang", "glycogen", "alphanumeric", "paragraph", "tryst"]

print("Welcone in paswword guessing game.")
print("Choose a difficulty level:  \nEASY\nMEDIUM\nHARD")

level = input("Enter-> ").lower()
if level == "easy":
    secret = random.choice(easy)
elif level == "medium":
    secret = random.choice(medium)
elif level == "hard":
    secret = random.choice(hard)
else:
    print("Kindly choose a valid level.")

attempts = 0
print("\nGuess the secret password")

while True:
    guess = input("Enter your guess: ").lower()
    attempts += 1

    if guess == secret:
        print(f"congratulations! You guessed in {attempts} attempts")
        break

    hint = ""

    for i in range(len(secret)):
        if i < len(guess) and guess[i] == secret[i]:
            hint += guess[i]
        else:
            hint += "_"
        
    print("Hint: ", hint)