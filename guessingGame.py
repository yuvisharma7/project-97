import random 
number = random.randint(1,9)
chances = 0
print("guess a number between 1 and 9")
while chances < 5: 
    guess = int(input("guess your number:"))

    if guess==number:
        print("coungratulations you won")
        break 
    elif guess<number: 
        print("your guess was too low:guess a higher number",guess)

    else:
        print("your guess was too high:guess a lower number",guess)

    chances += 1

if not chances <5: 
    print("you lose:the number is",number) 