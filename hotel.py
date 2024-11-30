MAX_RESERVATIONS = 50
MAX_STOCK_ITEMS = 4

room_stock = [2, 2, 2, 2]
package_stock = [2, 2, 2, 2]
kubo_stock = [2, 2, 2, 2]
food_stock = [2, 2, 2, 2]
drink_stock = [2, 2, 2, 2]

num_of_adults = [0] * MAX_RESERVATIONS
num_of_kids = [0] * MAX_RESERVATIONS
guest_names = [""] * MAX_RESERVATIONS
addresses = [""] * MAX_RESERVATIONS
phone_numbers = [""] * MAX_RESERVATIONS
check_in_dates = [""] * MAX_RESERVATIONS
check_in_times = [""] * MAX_RESERVATIONS
check_out_dates = [""] * MAX_RESERVATIONS
check_out_times = [""] * MAX_RESERVATIONS

def hotel_desk():
    print("\n1. Reservation")
    print("2. Rooms")
    print("3. Day Tour Package Offers")
    print("4. Kubo for Rent")
    print("5. Foods")
    print("6. Drinks")
    print("7. Activities")
    print("8. View Available Items")
    print("9. View History")
    print("10. Exit\n")

def rooms():
    print("\n1. Standard Room @ 1999", "2. StudioType @ 3999")
    print("3. Executive Room @ 4999")
    print("4. Bridal Room @ 6999\n")

def print_day_tour_packages():
    print("\n1. Swimming Pool Access + Lunch: @ 1999.00")
    print("2. Guided Nature Walk + Picnic: @ 2499.00")
    print("3. Beach Volleyball + Snacks: @ 1499.00")
    print("4. Island Hopping @ 4999.00\n")

def print_kubo_for_rent():
    print("\n1. Up to 3 persons @1500.00")
    print("2. Up to 6 persons @2500.00")
    print("3. Up to 9 persons @3999.00")
    print("4. Up to 15 persons @7999.00\n")

def foods():
    print("\n1. Fried Vegetables @ 219.00")
    print("2. Pork Sisig @ 329.00")
    print("3. Crispy Calamansi & Garlic Mayo Pie @ 269.00")
    print("4. Anghela's Mayo @ 949.00\n")

def drinks():
    print("\n1. Water @ 69.00")
    print("2. Mango Focus @ 139.00")
    print("3. WaterMelon Fix @ 179.00")
    print("4. Orange Fish Eye @ 160.00\n")

def activities():
    print("\n1. Floating Breakfast (Good for 2-3 pax) @ 2499.00")
    print("2. Signature Massage(good for 2pax) @ 1999.00")
    print("3. Swimming @ 1599.00")
    print("4. GYM (per-person) @ 500.00")

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

def update_stock(choice, selected_item, quantity):
    selected_stock = None

    if choice == 1:
        selected_stock = room_stock
    elif choice == 2:
        selected_stock = package_stock
    elif choice == 3:
        selected_stock = kubo_stock
    elif choice == 4:
        selected_stock = food_stock
    elif choice == 5:
        selected_stock = drink_stock
    else:
        print("Invalid choice!")
        return

    if selected_stock[selected_item - 1] < quantity:
        print("Insufficient stock for the selected item. Reservation not accepted.")
        return

    selected_stock[selected_item - 1] -= quantity

def view_available_items():
    print("\nAvailable Items to Reserve:")
    print("1. Rooms")

    for i in range(MAX_STOCK_ITEMS):
        print(f"{i + 1}. Room {i + 1} (Stock: {room_stock[i]})")
    print("\n-----------------------------")

    print("2. Day Tour Package Offers")
    for i in range(MAX_STOCK_ITEMS):
        print(f"{i + 1}. Package {i + 1} (Stock: {package_stock[i]})")
    print("\n-----------------------------")

    print("3. Kubo for Rent")
    for i in range(MAX_STOCK_ITEMS):
        print(f"{i + 1}. Kubo Option {i + 1} (Stock: {kubo_stock[i]})")
    print("\n-----------------------------")

    print("4. Foods")
    for i in range(MAX_STOCK_ITEMS):
        print(f"{i + 1}. Food {i + 1} (Stock: {food_stock[i]})")
    print("\n-----------------------------")

    print("5. Drinks")
    for i in range(MAX_STOCK_ITEMS):
        print(f"{i + 1}. Drink {i + 1} (Stock: {drink_stock[i]})")

def store_reservations():
    for i in range(MAX_RESERVATIONS):
        guest_names[i] = ""
        addresses[i] = ""
        phone_numbers[i] = ""
        num_of_adults[i] = 0
        num_of_kids[i] = 0
        check_in_dates[i] = ""
        check_in_times[i] = ""
        check_out_dates[i] = ""
        check_out_times[i] = ""

def view_history():
    print("\nCheck-in History:")
    is_empty = True
    for i in range(MAX_RESERVATIONS):
        if guest_names[i] != "":
            print("\n-----------------------------------------")
            print(f"Reservation ID: {i + 1}\n")
            print(f"Guest: {guest_names[i]}\n")
            print(f"Address: {addresses[i]}\n")
            print(f"Phone Number: {phone_numbers[i]}\n")
            print(f"Number of Adults: {num_of_adults[i]}\n")
            print(f"Number of Kids: {num_of_kids[i]}\n")
            print(f"Check-in Date: {check_in_dates[i]}\n")
            print(f"Check-in Time: {check_in_times[i]}\n")
            print(f"Check-out Date: {check_out_dates[i]}\n")
            print(f"Check-out Time: {check_out_times[i]}\n")
            is_empty = False
    if is_empty:
        print("There is no recorded history yet.\n")

def calculate_total(item_price, quantity):
    return item_price * quantity

def main():
    store_reservations()
    continue_guest = ""
    reservation_index = -1
    while True:
        choice, quantity, total = 0, 0, 0
        num_adults, num_kids = 0, 0
        pay, add_payment, charge = 0, 0, 0
        continue_choice = ""
        all_orders = ""
        guest_name, phone_number, address, check_in_date, check_in_time, check_out_date, check_out_time = "", "", "", "", "", "", ""

        print("\t\t\t\t\t\t************************")
        print("\n\t\t\t\t\t\t BEST RESORT AND HOTEL ")
        print("\n\t\t\t\t\t\t************************\n\n")

        print("\n\t\t\t\t\t***WELCOME MA'AM & SIR TO MAYARI RESORT AND HOTEL.***\nWe are delighted to have you as our guest and look forward to providing you an unforgettable stay. Please let me or anyone on the staff know if there is anything we can do for you throughout your time with us.\n\n")
        print("\n---------------------------------------------- ")
        print("\n\t\tMAIN MENU")
        print("\n---------------------------------------------- ")

        while True:
            hotel_desk()
            choice = int(input("\nEnter your Choice Ma'am/Sir: "))

            if choice == 1:
                for i in range(MAX_RESERVATIONS):
                    if guest_names[i] == "":
                        reservation_index = i
                        break
                if reservation_index == -1:
                    print("\nSorry, all reservations are full. Please try again later.\n")
                    break
                guest_name, phone_number, address, num_adults, num_kids, check_in_date, check_in_time, check_out_date, check_out_time = collect_reservation_info()

                print("\n-----------------------------")
                print("\nReservation Details:\n")
                print(f"Guest Name: {guest_name}")
                print(f"Phone Number: {phone_number}")
                print(f"Address: {address}")
                print(f"Number of Adults: {num_adults}")
                print(f"Number of Kids: {num_kids}")
                print(f"Select your preferred Check-in Date: {check_in_date}")
                print(f"Check-in Time: {check_in_time}")
                print(f"Check-out Date: {check_out_date}")
                print(f"Check-out Time: {check_out_time}")
                print("\n-----------------------------")

                guest_names[reservation_index] = guest_name
                addresses[reservation_index] = address
                phone_numbers[reservation_index] = phone_number
                num_of_adults[reservation_index] = num_adults
                num_of_kids[reservation_index] = num_kids
                check_in_dates[reservation_index] = check_in_date
                check_in_times[reservation_index] = check_in_time
                check_out_dates[reservation_index] = check_out_date
                check_out_times[reservation_index] = check_out_time

                print(f"\nReservation successful! Your reservation ID is: {reservation_index + 1}")
                reservation_index = -1

                continue_choice = input("\nDo you want to continue browsing the main menu? (yes/no): ")
                if continue_choice.lower() == "no":
                    break
                continue  # Return to the main menu

            elif choice == 2:
                rooms()
            elif choice == 3:
                print_day_tour_packages()
            elif choice == 4:
                print_kubo_for_rent()
            elif choice == 5:
                foods()
            elif choice == 6:
                drinks()
            elif choice == 7:
                activities()
            elif choice == 8:
                view_available_items()
                continue_choice = input("\nDo you want to continue browsing the main menu? (yes/no): ")
                if continue_choice.lower() == "yes":
                    continue
            elif choice == 9:
                view_history()
                continue_choice = input("\nDo you want to continue browsing the main menu? (yes/no): ")
                if continue_choice.lower() == "yes":
                    break
                continue
            elif choice == 10:
                print("Thank you for visiting Mayari Resort and Hotel. Have a great day!\n")
                print("\n-----------------------------")
                print("Contact us:\nata.liraangela.r@gmail.com\nPhone Number: 09984996493\nFacebook Account: MAYARI SIMPLE RESORT AND HOTEL")
                return
            else:
                print("Invalid choice! Please try again.\n")
                continue

            selected_item = int(input("\nEnter the item choice: "))
            price = 0.0
            item_name = ""

            if choice == 1:
                continue  # Skip item selection for reservation
            elif choice == 2:
                if selected_item == 1:
                    price = 1999.0
                    item_name = "Standard Room"
                elif selected_item == 2:
                    price = 3999.0
                    item_name = "StudioType"
                elif selected_item == 3:
                    price = 4999.0
                    item_name = "Executive Room"
                elif selected_item == 4:
                    price = 6999.0
                    item_name = "Bridal Room"
                else:
                    print("Invalid item. Please try again.\n")
                    continue
            elif choice == 3:
                if selected_item == 1:
                    price = 1999.0
                    item_name = "Swimming Pool Access + Lunch"
                elif selected_item == 2:
                    price = 2499.0
                    item_name = "Guided Nature Walk + Picnic"
                elif selected_item == 3:
                    price = 1499.0
                    item_name = "Beach Volleyball"
                elif selected_item == 4:
                    price = 4999.0
                    item_name = "Island Hopping"
                else:
                    print("Invalid item. Please try again.\n")
                    continue
            elif choice == 4:
                if selected_item == 1:
                    price = 1500.0
                    item_name = "Up to 3 persons"
                elif selected_item == 2:
                    price = 2500.0
                    item_name = "Up to 6 persons"
                elif selected_item == 3:
                    price = 3999.0
                    item_name = "Up to 9 persons"
                elif selected_item == 4:
                    price = 7999.0
                    item_name = "Up to 15 persons"
                else:
                    print("Invalid item . Please try again.\n")
                    continue
            elif choice == 5:
                if selected_item == 1:
                    price = 219.0
                    item_name = "Fried Vegetables"
                elif selected_item == 2:
                    price = 329.0
                    item_name = "Pork Sisig"
                elif selected_item == 3:
                    price = 269.0
                    item_name = "Crispy Calamansi & Garlic Mayo Pie"
                elif selected_item == 4:
                    price = 949.0
                    item_name = "Anghela's Mayo"
                else:
                    print("Invalid item. Please try again.\n")
                    continue
            elif choice == 6:
                if selected_item == 1:
                    price = 69.0
                    item_name = "Water"
                elif selected_item == 2:
                    price = 139.0
                    item_name = "Mango Focus"
                elif selected_item == 3:
                    price = 179.0
                    item_name = "WaterMelon Fix"
                elif selected_item == 4:
                    price = 160.0
                    item_name = "Orange Fish Eye"
                else:
                    print("Invalid item. Please try again.\n")
                    continue
            elif choice == 7:
                if selected_item == 1:
                    price = 2499.0
                    item_name = "Floating Breakfast"
                elif selected_item == 2:
                    price = 1999.0
                    item_name = "Signature Massage"
                elif selected_item == 3:
                    price = 1599.0
                    item_name = "Swimming"
                elif selected_item == 4:
                    price = 500.0
                    item_name = "GYM"
                else:
                    print("Invalid item. Please try again.\n")
                    continue
            else:
                print("Invalid choice! Please try again.\n")
                continue

            quantity = int(input("Enter the quantity: "))
            total += calculate_total(price, quantity)  # Correct calculation of the total
            update_stock(choice, selected_item, quantity)  # Now correctly update the stock after calculating total
            all_orders += f"{item_name} x{quantity}\n"

            continue_choice = input("Do you want to continue to choose, Ma'am and Sir? (yes, no): ")
            if continue_choice.lower() == "no":
                break

        while pay < total:
            print(f"Current total: PHP {total}")
            add_payment = float(input("\nEnter payment: PHP "))
            if pay + add_payment < total:
                print("Insufficient payment, please add more.")
            else:
                pay += add_payment

        charge = pay - total
        print(f"Your change is: PHP {charge}")

        print("\n-----------------RECEIPT----------------")
        print("\nReservation Details:\n")
        print(f"Guest Name: {guest_name}")
        print(f"Phone Number: {phone_number}")
        print(f"Address: {address}")
        print(f"Number of Adults: {num_adults}")
        print(f"Number of Kids: {num_kids}")
        print(f"Check-in Date: {check_in_date}")
        print(f"Check-in Time: {check_in_time}")
        print(f"Check-out Date: {check_out_date}")
        print(f"Check-out Time: {check_out_time}")
        print("\n-----------------------------")
        print("\nYour Reserved:\n" + all_orders)
        print("\nThank you for visiting us at MAYARI RESORT AND HOTEL.\nWe hope we achieved our goal of making your stay memorable by providing outstanding service.")
        continue_guest = input("\nIs there another guest, Ma'am/Sir? (yes/no): ")

if __name__ == "__main__":
    main()
