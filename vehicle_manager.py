class Vehicle:
    def __init__(self, brand, model, mileage, service_date):
        self.brand = brand
        self.model = model
        self.mileage = mileage
        self.service_date = service_date

def list_all_vehicles(vehicles):
    for index, vehicle in enumerate(vehicles):
        print "ID:" + str(index)
        print "Brand:", vehicle.brand
        print "Model:", vehicle.model
        print "Mileage:", vehicle.mileage
        print "Service date:", vehicle.service_date
        print ""

    if not vehicles:
        print "There are no vehicles in the list."

def add_new_vehicle(vehicles):
    brand = raw_input("Enter the brand of the vehicle: ")
    model = raw_input("Enter the model of the vehicle: ")
    mileage = raw_input("Enter the mileage of the vehicle: ")
    service_date = raw_input("Enter general service date for the vehicle: ")

    new = Vehicle(brand=brand, model=model, mileage=mileage, service_date=service_date)
    vehicles.append(new)

    print "%s %s was successfully added to the list." % (brand, model)

def select_vehicle(vehicles):
    print "Select the ID of the vehicle you'd like to edit:"

    for index, vehicle in enumerate(vehicles):
        print str(index) + ") ", vehicle.brand, vehicle.model

    selected_id = raw_input("Which vehicle would you like to edit? (enter ID number): ")
    return vehicles[int(selected_id)]

def edit_mileage(vehicles):
    selected_vehicle = select_vehicle(vehicles)
    new_mileage = raw_input("Enter new mileage for %s: " % selected_vehicle.model)
    selected_vehicle.mileage = new_mileage

    print ""
    print "Mileage updated."

def edit_service_date(vehicles):
    selected_vehicle = select_vehicle(vehicles)
    new_service_date = raw_input("Enter new service date for %s: " % selected_vehicle.model)
    selected_vehicle.service_date = new_service_date

    print ""
    print "Service date updated."

def write_file(vehicles):
    with open("vehicle_manager.txt", "w+") as vehicle_file:
        for vehicle in vehicles:
            vehicle_file.write("%s, %s, %s, %s\n" % (vehicle.brand, vehicle.model, vehicle.mileage, vehicle.service_date))

def main():
    print "Welcome to the Vehicle Manager"

    vehicles = []

    while True:
        print ""
        print "Please select one of the options:"
        print "a) See all vehicles"
        print "b) Add a vehicle"
        print "c) Update mileage"
        print "d) Update service date"
        print "e) Quit the program."
        print ""

        selection = raw_input("Enter your selection: ")
        print ""

        if selection.lower() == "a":
            list_all_vehicles(vehicles)
        elif selection.lower() == "b":
            add_new_vehicle(vehicles)
        elif selection.lower() == "c":
            edit_mileage(vehicles)
        elif selection.lower() == "d":
            edit_service_date(vehicles)
        elif selection.lower() == "e":
            print "Thanks for the visit. Bye."
            write_file(vehicles)
            break
        else:
            print "Invalid selection. Try again."
            continue

if __name__ == '__main__':
    main()