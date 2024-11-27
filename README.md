#hotelmanagement

# Global lists to store stock items and reservation history
room_inventory = {"Standard Room": 10, "StudioType": 5, "Executive Room": 3, "Bridal Room": 2}
kubo_inventory = {3: 10, 6: 5, 9: 3, 15: 2}
food_inventory = {"Fried Vegetables": 20, "Pork Sisig": 10, "Crispy Calamansi & Garlic Mayo Pie": 15, "Anghela's Mayo": 8}
drink_inventory = {"Water": 50, "Mango Focus": 30, "WaterMelon Fix": 20, "Orange Fish Eye": 25}
activity_inventory = {"Floating Breakfast": 5, "Signature Massage": 3, "Swimming": 10, "GYM": 20}

reservations = []  # List to hold reservations
history = []  # List to store history of actions

def hotel_desk():
    print("\n1. Rooms\n2. Day Tour Package Offers\n")
    print("3. Kubo for Rent\n4. Foods\n")
    print("5. Drinks\n6. Activities\n")
    print("7. View Available Items\n")
    print("8. Reservation Form\n")
    print("9. View History\n")
    print("10. Exit\n")

def rooms():
    print("\n1. Standard Room @ 1999\n2. StudioType @ 3999\n")
    print("3. Executive Room @ 4999\n4. Bridal Room @ 6999\n")

def print_day_tour_packages():
    print("\n1. Swimming Pool Access + Lunch: @ 1999.00\n")
    print("2. Guided Nature Walk + Picnic: @ 2499.00\n")
    print("3. Beach Volleyball + Snacks: @ 1499.00\n4. Island Hopping @ 4999.00\n")

def print_kubo_for_rent():
    print("\n1. Up to 3 persons @1500.00\n2. Up to 6 persons @2500.00\n")
    print("3. Up to 9 persons @3999.00\n4. Up to 15 persons @7999.00\n")

def foods():
    print("\n1. Fried Vegetables @ 219.00\n2. Pork Sisig @ 329.00\n")
    print("3. Crispy Calamansi & Garlic Mayo Pie @ 269.00\n4. Anghela's Mayo @ 949.00\n")

def drinks():
    print("\n1. Water @ 69.00\n2. Mango Focus @ 139.00\n")
    print("3. WaterMelon Fix @ 179.00\n4. Orange Fish Eye @ 160.00\n")

def activities():
    print("\n1. Floating Breakfast (Good for 2-3 pax) @ 2499.00\n2. Signature Massage(good for 2pax) @ 1999.00\n")
    print("3. Swimming @ 1599.00\n4. GYM (per-person) @ 500.00")

def collect_reservation_info():
    guest_name = input("\nGuest Name: ")
    phone_number = input("Phone Number: ")
    address = input("Address: ")
    num_adults = int(input("Number of Adults: "))
    num_kids = int(input("Number of Kids: "))
    check_in_date = input("Check-in Date (DD-MM-YYYY): ")
    check_in_time = input("Check-in Time (HH:MM): ")
    check_out_date = input("Check-out Date (DD-MM-YYYY): ")
    check_out_time = input("Check-out Time (HH:MM): ")
    return guest_name, phone_number, address, num_adults, num_kids, check_in_date, check_in_time, check_out_date, check_out_time

def view_available_items():
    print("\nRooms Availability:")
    for room, qty in room_inventory.items():
        print(f"{room}: {qty} available")
    print("\nKubo Rentals Availability:")
    for persons, qty in kubo_inventory.items():
        print(f"Up to {persons} persons: {qty} available")
    print("\nFood Items Availability:")
    for food, qty in food_inventory.items():
        print(f"{food}: {qty} available")
    print("\nDrinks Availability:")
    for drink, qty in drink_inventory.items():
        print(f"{drink}: {qty} available")
    print("\nActivity Availability:")
    for activity, qty in activity_inventory.items():
        print(f"{activity}: {qty} available")

def make_reservation():
    guest_name, phone_number, address, num_adults, num_kids, check_in_date, check_in_time, check_out_date, check_out_time = collect_reservation_info()
    reservation = {
        "Guest Name": guest_name,
        "Phone Number": phone_number,
        "Address": address,
        "Adults": num_adults,
        "Kids": num_kids,
        "Check-in Date": check_in_date,
        "Check-in Time": check_in_time,
        "Check-out Date": check_out_date,
        "Check-out Time": check_out_time
    }
    reservations.append(reservation)
    history.append(f"Reservation made by {guest_name} on {check_in_date} from {check_in_time}")
    print(f"\nReservation made for {guest_name}!")

def view_history():
    print("\nReservation History:")
    if not history:
        print("No history available.")
    for record in history:
        print(record)

def hotel_management_system():
    while True:
        hotel_desk()
        choice = int(input("\nEnter choice: "))

        if choice == 1:
            rooms()
        elif choice == 2:
            print_day_tour_packages()
        elif choice == 3:
            print_kubo_for_rent()
        elif choice == 4:
            foods()
        elif choice == 5:
            drinks()
        elif choice == 6:
            activities()
        elif choice == 7:
            view_available_items()
        elif choice == 8:
            make_reservation()
        elif choice == 9:
            view_history()
        elif choice == 10:
            print("Thank you for using the Hotel Management System!")
            break
        else:
            print("Invalid choice! Please try again.")

# Run the hotel management system
hotel_management_system()
