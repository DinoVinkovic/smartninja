import random

def lottery_numbers_generator(quantity):
    lottery_numbers = []

    while len(lottery_numbers) < quantity:
        number = random.randint(1, 45)
        if number not in lottery_numbers:
            lottery_numbers.append(number)
    return lottery_numbers

quantity = int(raw_input("How many numbers would you like to have? "))

print lottery_numbers_generator(quantity)