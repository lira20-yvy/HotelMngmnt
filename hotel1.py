#hotelmanagement


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
#need my stocks
#need maglagay reservations
#pwede rin hitsory
