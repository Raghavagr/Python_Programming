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
