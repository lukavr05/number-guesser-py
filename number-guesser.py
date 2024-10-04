import random
import time

class GuessBot():
    def __init__(self, maxInt):
        self.numOfGuesses = 0
        self.finished = true
        self.max = maxInt
        self.previousGuess = 0

    def guess(self, accuracy):
    # -1 for too low, 1 for too high and 0 for correct
        if accuracy < 0:
            n = (self.max - self.previousGuess) // 2
            self.previousGuess = n
            self.numOfGuesses++
            print("GuessBot guessed", n)
            return n
        elif accuracy > 0:
            n = self.previousGuess // 2


def manual():
    max = int(input("Enter maximum value:  "))
    target = random.randint(1, max)

    print("\nGenerating number...\n")
    time.sleep(2)
    
    guess = int(input("Enter your guess:  "))
    if guess == target:
        print("WOW! You guessed it first try!")
    else:
        guessCount = 1
        while guess != target:
            if guess > target:
                print("Guess lower!")
            else:
                print("Guess higher!")
            guessCount += 1
            guess = int(input("Enter your guess:  "))

        print("You guessed the number in", guessCount, "guesses!")

    
def automatic():
    pass

def main():
    print("="*50)
    print("Welcome to the Random Number Guessing Game!!!")
    print("="*50)

    print("\nChoose Automatic Mode (1) or Manual Mode (2)\n")

    modeSelect = int(input(">> "))

    if modeSelect == 1:
        print("Automatic mode selected!")
        automatic()
    else:
        print("Manual mode selected!")
        manual()

main()
