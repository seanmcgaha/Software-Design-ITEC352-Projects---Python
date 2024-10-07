import csv
import os

ARP_FILENAME = "File_Week_5_Assignment.csv"
TRIP_FILENAME = "entries.csv"

def create_sample_arp_file():
    if not os.path.exists(ARP_FILENAME):
        with open(ARP_FILENAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["192.168.1.1", "00:1A:2B:3C:4D:5E"])
            writer.writerow(["192.168.1.2", "00:1A:2B:3C:4D:5F"])

def create_sample_trips_file():
    if not os.path.exists(TRIP_FILENAME):
        with open(TRIP_FILENAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["100", "5", "20.00"])
            writer.writerow(["200", "10", "20.00"])


def read_entries():
    arpentries = []
    with open(ARP_FILENAME, newline ="") as file:
        reader = csv.reader(file)
        for row in reader:
            arpentries.append(row)
    return arpentries

def write_entries(arpentries):
    with open(ARP_FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(arpentries)

def read_trips():
    trips = []
    with open(TRIP_FILENAME, newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            trips.append(row)
    return trips

def write_trips(trips):
    with open(TRIP_FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(trips)

def display_arp_menu():
    print ("welcome to the arp entries application")
    print()
    print("1 - List Entries")
    print("2 - add entries")
    print("3 - delete entries")
    print("4 - exit")

def list_entries(arpentries):
    if arpentries:
        for i, entry in enumerate(arpentries, start=1):
            print(f"{i}. {', '.join(entry)}")
    else:
        print("no entries found.")

def add_entry(arpentries):
    ip_add = input("Please enter an IP address: ")
    mac_add = input("Please enter a mac address")
    entry = [ip_add, mac_add]
    arpentries.append(entry)
    print("Entry added to list")

def delete_entry(arpentries):
    index = int(input("Which number would you like to delete? "))
    if index <1 or index > len(arpentries):
        print("invalid entry number")
    else:
        arpentries.pop(index -1)
        print("Entry was deleted")
        write_entries(arpentries)

def display_trip_menu():
    print("\nWelcome to the Trip Management Application")
    print("1 - List Trips")
    print("2 - Add Trip")
    print("3 - Exit")

def list_trips(trips):
    if trips:
        for i, trip in enumerate(trips, start=1):
            print(f"{i}. {', '.join(trip)}")
    else:
        print("No trips found.")

def add_trip(trips):
    miles = float(input("Please enter miles driven: "))
    gallons = float(input("Please enter the gallons used: "))
    mpg = miles / gallons
    trip = [str(miles), str(gallons), f"{mpg:.2f}"]
    trips.append(trip)
    print(f"Trip added with MPG: {mpg:.2f}")

def main():

    create_sample_arp_file()
    create_sample_trips_file()

    arpentries = read_entries()
    trips = read_trips()

    while True:
        display_arp_menu()
        usercmd = input("Please enter an option: ")
        match usercmd:
            case "1":
                list_entries(arpentries)
            case "2":
                add_entry(arpentries)
                write_entries(arpentries)
            case "3":
                delete_entry(arpentries)
            case "4":
                break
            case _:
                print("Not a valid command. Please try again.\n")

    while True:
        display_trip_menu()
        usercmd = input("Please enter an option: ")
        match usercmd:
            case "1":
                list_trips(trips)
            case "2":
                add_trip(trips)
                write_trips(trips)
            case "3":
                break
            case _:
                print("Not a valid command. Please try again. \n")



if __name__ == "__main__":
    main()
    