import random

def get_word():
    words = ['cat','dog','mouse','snake','lion','monkey','horse']
    return random.choice(words)

def play_game():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    word = get_word()
    letters_guessed = []
    tries =10
    guessed =  False

    #hint
    print('the word contains',len(word),' letters')
    #spaces
    print(len(word) * '*')

    while guessed == False and tries > 0:
        print("you have"+str(tries)+" tries")
        guess = input("please enter a letter or a full word").lower()

        #1 - user input a letter
        if len(guess)==1:
            if guess not in alphabet:
                print("you have not enter a letter")
            elif guess in letters_guessed:
                print("you have already guessed this letter")
            elif guess not in word:
                print("sry, this letter not part of word")
            elif guess in word:
                print("well done, letter exist in word")
                letters_guessed.append(guess)
            else:
                print("No idea about this message, it should be investigated")

        #2 - User inputs a word
        elif len(guess) == len(word):
            if guess == word:
                print("Well Done! you guess word")
                guessed = True
            else:
                print("Sorry, that's not the word")
                tries -= 1
        
        #3 -User inputs letter where total no. of letters =/= total no. of letter in word
        else:
            print("the length of your guess is not same as length of word, we are looking for..")

        status = ''
        if guessed == False:
            for letter in word:
                if letter in letters_guessed:
                    status += letter
                else:
                    status += '*'
            print(status)

        if status == word:
            print("Well Done!, you have guessed a word correctly")
            guessed = True
        elif tries == 0:
            print("you have run out of no. of guesses you have & you haven't guessed the word")

play_game()