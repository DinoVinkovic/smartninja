import random

def main():
    hidden_number = random.randint(1, 100)
    user_guess = 0

    while not user_guess == hidden_number:
        user_guess = int(raw_input("Guess the secret number between 0 and 100: "))

        if user_guess == hidden_number:
            print "That's right!"
        elif user_guess < hidden_number:
            print "Nope. Try higher."
        elif user_guess > hidden_number:
            print "Nope. Try lower."

if __name__ == '__main__':
    main()
