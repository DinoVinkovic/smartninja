secret = 21

guess = int(raw_input("Guess the secret number between 0 and 50: "))

if guess == secret:
    print "Congratz!"
elif guess < secret:
    print "Nope. Try higher."
elif guess > secret:
    print "Nope. Try lower."
else:
    print "Not a number!"