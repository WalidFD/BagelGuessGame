import random
from unicodedata import name

Num_digits = 3
Max_guess = 10

def main():
    print(f'''Bagels, a deductive logic game. I am thinking of a {Num_digits}-digit number with no repeated digits.
    Try to guess what it is. Here are some clues:
    When I say: That means:
    Pico One digit is correct but in the wrong position.
    Fermi One digit is correct and in the right position.
    Bagels No digit is correct.
For example, if the secret number was 248 and your guess was 843, the
 clues would be Fermi Pico.''')

    while True : 
        Scn = getSecretNum()
        print("I have Thought up a Number")
        print(f"You have {Max_guess} guesses to get it ")
        NumG = 1
        while NumG <= Max_guess:
            guess = ''
            while len(guess) != Num_digits or not guess.isdecimal():
                print(f"Guess# {NumG}")
                guess = input('')

            clues = getClues(guess,Scn)
            print(clues)
            NumG +=1

            if guess == Scn:
                break
            if NumG > Max_guess:
                print("You run out of guesses")
                print(f"The answer was {Scn}")

        print("Do you Want to play again ? () yes or no")
        if not input(" ").lower().startswith("y"):
            break
    print("Thanks for playing !")


def getSecretNum():
    Numb = list('0123456789')
    random.shuffle(Numb)
    Scn = ''
    for i in range(Num_digits):
        Scn += str(Numb[i])
    return Scn

def getClues(guess , Scn):
    if guess == Scn :
        print("You got it !")
        
    clues = []

    for i in range(len(guess)):
        if guess[i] == Scn[i]:
            clues.append("fermi")
        elif guess[i] in Scn:
            clues.append("pico")

    if len(clues) == 0:
        print("bagels")
    else:
        print(' '.join(clues))

if __name__=='__main__':
    main()
    