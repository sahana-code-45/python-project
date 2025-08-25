import random

number = random.randint(1,100)
guess = 0
count = 0
max_attempts = 7

while  count < max_attempts :

# Prevent User from Entering invalid inputs
    try :
     guess = int(input("\nEnter the Guess: "))
    except ValueError :
        print("Error: Invalid Input! Please enter a number")
        continue
    count = count + 1

# Number guessed higer or lower
    if guess > number :
        print("\nGuess Lower")
    elif guess < number :
        print("\nGuess Higher") 
    else : 
        print("\n\n You Won !!")
        break

# How many attmpts left
    if  count < max_attempts :
        print("\nOnly Fewer Attempts left",max_attempts - count)
    
    elif count == max_attempts :
        print("\n\nMaximum Attempts Reached")

# if loop ends without guessing correctly
if guess != number :
    print("\n\nMaximum Attempts Reached.  The number was:", number)
