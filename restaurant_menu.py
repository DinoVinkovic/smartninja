print "Restaurant menu"

menu = {}

while True:
    dish = raw_input("Please enter the name of a dish: ")
    price = raw_input("What's the price of the dish: ")

    while price.isalpha():
        print "Not a number."
        price = raw_input("What's the price of the dish: ")

    print "Your dish " + dish + " costs " + price + " HRK."
    menu[dish] = price

    new = raw_input("Would you like to enter a new dish? Y / N ")

    if new == "N" or new == "n":
        break


res_menu = open("restaurant_menu.txt", "w+")

print "Restaurant menu: "
res_menu.write("Menu:\n")
for dish in menu:
    print dish + ": " + menu[dish] + " HRK"
    res_menu.write(dish + ": " + menu[dish] + " HRK" + "\n")

res_menu.write("\n")
res_menu.close()

print "END"