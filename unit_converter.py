print "-- Unit Converter --"

while True:
    km = raw_input("Enter a number: ")
    while not km.isdigit():
        print "Not an integer."
        km = raw_input("Please, enter a number: ")

    mi = int(km) * 0.62
    print str(km), "kilometers equals to", str(mi), "miles."

    answer = raw_input("Do you want to do another conversion? (Y / N) ")
    while (answer != "y" and answer != "Y") and (answer != "n" and answer != "N"):
        answer = raw_input("Please, enter Y or N: ")
    if answer == "y" or answer == "Y":
        continue
    elif answer == "n" or answer == "N":
        print "End of program"
        break