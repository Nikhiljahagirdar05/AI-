
# Intelligent Agent - Number Guessing

# Initial guessing range
low = 1
high = 100

print("Think of a number between 1 and 100.")

while low <= high:

    # Guess the middle number
    guess = (low + high) // 2

    print("\nMy guess is:", guess)

    print("H - Your number is Higher")
    print("L - Your number is Lower")
    print("C - My guess is Correct")

    # Take feedback from user
    feedback = input("Enter H, L or C: ").upper()

    # Update the range
    if feedback == "H":

        low = guess + 1

    elif feedback == "L":

        high = guess - 1

    elif feedback == "C":

        print("Correct! I guessed your number.")
        break

    else:

        print("Invalid input! Please enter H, L or C.")

else:

    print("Invalid feedback or inconsistent answers.")
