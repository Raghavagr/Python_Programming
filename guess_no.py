import random
secret = random.randrange(1,100)
print(secret)
guess=0
trials=0
while guess!=secret:
    guess = int(input("Enter your guess:-"))
    trials = trials + 1
    if guess > secret:
        print("Guess Too High")
    elif guess < secret:
        print("Guess Too Low")
    else:
        print("Yeahh! You Got it,")
        print("Its Correct")
print("\nThe total no. of Guess made:",trials)


# SOME OTHER CODE:
## URL: https://ide.geeksforgeeks.org/iGGBmFoj3q

##one more interesting code in different way:
# URL: https://ide.geeksforgeeks.org/aN52wItX3G

## Guess Number Between Player-1 and Player-2
# URL:  https://ide.geeksforgeeks.org/JQcAqPY34F

### MODIFIED PROGRAM BETWEEN PLAYER-1 AND PLAYER-2 IN PYTHONIC WAY...
# URL:  https://ide.geeksforgeeks.org/6B710hENPo
