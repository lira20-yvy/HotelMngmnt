import random
import csv
from termcolor import colored

def load_stock(filename):
    stock = {}
    default_stock = {
        'rooms': [3, 3, 3, 2],
        'packages': [3, 2, 2, 2],
        'foods': [3, 3, 2, 2],
    }
    try:
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                item_type, *values = row
                stock[item_type] = list(map(int, values))
    except FileNotFoundError:
        print(f"{filename} not found.")
        stock = default_stock
        save_stock(filename, stock)
    return stock

def save_stock(filename, stock):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["item_type", "item1", "item2", "item3", "item4"])
        for item_type, values in stock.items():
            writer.writerow([item_type] + values)

item_prices = {
    'rooms': [1999, 3999, 4999, 6999],
    'packages': [1999, 1499, 1499, 999],
    'foods': [2599, 600, 3000, 949],
}

def hotel_desk():
    print("\n Available on MAYARI'S SIMPLY HOTEL")
    print("\n1. Reservation form")
    print("2. Rooms")
    print("3. Day Tour Package Offers")
    print("4. Foods")
    print("5. Exit\n")

def rooms():
    print("\n1. Standard Room @ 1999 / 2. Studio Type @ 3999 / 3. Executive Room @ 4999 / 4. Bridal Room @ 6999")

def print_day_tour_packages():
    print("\n1. Swimming Pool Access: @ 1999.00 / 2. Kids’ Play Area and Activities: @ 1499.00 / 3. Photography Tours: @ 1499.00 / 4. Spa and Wellness Treatments @ 999.00")

def foods():
    print("\n1. (3 Pax) Unlimited Samgyup and Wings @ 2599.00  / 2. (2 Pax) Bundle Spaghetti, Chicken and Fries @ 600.00 / 3. Full day Access Buffet @ 3000.00 / 4. Dinner at Hotel @ 949.00")

def collect_reservation_info():
    print(colored("\nPlease provide the following details below, Ma'am and Sir.", "cyan"))
    guest_name = input("\nGuest Name: ")
    phone_number = input("Phone Number: ")
    address = input("Address: ")
    while True:
        try:
            num_adults = int(input("Number of Adults: "))
            num_kids = int(input("Number of Kids: "))
            break
        except ValueError:
            print("Invalid input! Please enter numbers only.")
    arrival_date = input("Arrival Date (DD-MM-YYYY): ")
    arrival_time = input("Arrival Time: ")
    return guest_name, phone_number, address, num_adults, num_kids, arrival_date, arrival_time

def update_stock(stock, item_type, selected_item, quantity):
    if stock[item_type][selected_item - 1] < quantity:
        print(colored("\nThis item is reserved by another guest. Please choose another one.", "red"))
        return False
    stock[item_type][selected_item - 1] -= quantity
    return True

def calculate_total(item_price, quantity):
    return item_price * quantity

def get_price_and_name(choice, selected_item):
    if choice == 2:
        return item_prices['rooms'][selected_item - 1], f"Room {selected_item}"
    elif choice == 3:
        return item_prices['packages'][selected_item - 1], f"Package {selected_item}"
    elif choice == 4:
        return item_prices['foods'][selected_item - 1], f"Food {selected_item}"
    else:
        print("Invalid choice!")
        return 0, ""

def random_promotion():
    promotions = [
        "10% off on your next booking!", "Free drink with every meal order!", "Complimentary spa for every room booking!"
    ]
    print("\n🎉 Today's Promotion:", random.choice(promotions))


def collect_feedback():
    while True:
        try:
            rating = int(input("\nRate your experience (1-5): "))
            if 1 <= rating <= 5:
                break
            else:
                print("Please enter a valid rating between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")

    comment = input("Additional comments: ")
    print(f"Thank you for your feedback!! \nRating: {rating}/5 - \nComment: {comment}")

def main():
    stock_filename = "stocks.csv"
    stock = load_stock(stock_filename)

    while True:
        choice, quantity, total = 0, 0, 0
        pay, add_payment, charge = 0, 0, 0
        all_orders = ""
        guest_name, phone_number, address, arrival_date, arrival_time = "", "", "", "", ""

        print(colored("\n\t\t\t\t\t***WELCOME MA'AM & SIR TO MAYARI SIMPLY HOTEL.***\nWe are delighted to have you as our guest and look forward to providing you an unforgettable stay. Please let me or anyone on the staff know if there is anything we can do for you throughout your time with us.\n\n", "blue"))
        print(colored("\n---------------------------------------------- ", "blue"))
        print(colored("\n\t\tMAIN MENU", "blue"))
        print(colored("\n---------------------------------------------- ", "blue"))

        while True:
            hotel_desk()
            try:
                choice = int(input(colored("\nEnter your Choice Ma'am/Sir: ", "blue")))
                if choice not in [1, 2, 3, 4, 5]:
                    raise ValueError("Invalid menu option.")
            except ValueError:
                print("Invalid input! Please enter a valid menu option (1-5).")
                continue

            if choice == 1:
                guest_name, phone_number, address, num_adults, num_kids, arrival_date, arrival_time = collect_reservation_info()

                print("\n-----------------------------")
                print("\nReservation Details:\n")
                print(f"Guest Name: {guest_name}")
                print(f"Phone Number: {phone_number}")
                print(f"Address: {address}")
                print(f"Number of Adults: {num_adults}")
                print(f"Number of Kids: {num_kids}")
                print(f"Arrival Date: {arrival_date}")
                print(f"Arrival Time: {arrival_time}")
                print("\n-----------------------------")

                random_promotion()

                continue_choice = input(colored("\nDo you want to continue browsing the main menu? (yes/no): ", "cyan"))
                if continue_choice.lower() == "no":
                    break
                continue

            elif choice == 2:
                rooms()
            elif choice == 3:
                print_day_tour_packages()
            elif choice == 4:
                foods()
            elif choice == 5:  # Exit option
                print("Thank you for your visit. Have a great day!")
                save_stock(stock_filename, stock)
                return  # Exit the program

            while True:
                try:
                    selected_item = int(input("\nEnter the item choice: "))
                    if selected_item < 1 or selected_item > 4:
                        raise ValueError("Invalid item choice.")
                except ValueError:
                    print("Invalid input! Please select a valid item (1-4).")
                    continue

                price, item_name = get_price_and_name(choice, selected_item)

                if price == 0:
                    continue

                try:
                    quantity = int(input("Enter the quantity: "))
                    if quantity <= 0:
                        raise ValueError("Quantity must be positive.")
                except ValueError:
                    print("Invalid input! Please enter a positive number for quantity.")
                    continue

                if update_stock(stock, ['rooms', 'packages', 'foods'][choice - 2], selected_item, quantity):
                    break

            total += calculate_total(price, quantity)

            # Update all_orders with the current order
            all_orders += f"{item_name} (x{quantity}) - PHP {calculate_total(price, quantity)}\n"

            continue_choice = input(colored("Do you want to continue to choose, Ma'am and Sir? (yes, no): ", "cyan"))
            if continue_choice.lower() == "no":
                break

        while pay < total:
            print(f"\nCurrent total: PHP {total}")
            try:
                add_payment = float(input("\nEnter payment: PHP "))
                if add_payment <= 0:
                    raise ValueError("Payment must be positive.")
                pay += add_payment
                if pay < total:
                    print("Insufficient payment, please add more.")
            except ValueError:
                print("Invalid input! Please enter a valid number.")
                continue

        charge = pay - total
        print(f"Your change is: PHP {charge}")

        print("\n-----------------RECEIPT----------------")
        print(colored("\nReservation Details:\n", "cyan"))
        print(colored(f"Guest Name: {guest_name}", "cyan"))
        print(colored(f"Phone Number: {phone_number}", "cyan"))
        print(colored(f"Address: {address}", "cyan"))
        print(colored(f"Number of Adults: {num_adults}", "cyan"))
        print(colored(f"Number of Kids: {num_kids}", "cyan"))
        print(colored(f"Arrival Date: {arrival_date}", "cyan"))
        print(colored(f"Arrival Time: {arrival_time}", "cyan"))
        print(colored("\n-----------------------------", "cyan"))
        print(colored("\nReference from: @mayarisimplyhotel@gmail.com", "cyan"))
        print("\nYour Reserved:\n" + all_orders)

        print(colored("\nThank you for visiting us at MAYARI SIMPLY HOTEL.\nWe hope we achieved our goal of making your stay memorable by providing outstanding service.", "blue"))

        continue_guest = input("\nIs there another guest, Ma'am/Sir? (yes/no): ")
        collect_feedback()
        if continue_guest.lower() == "no":
            print("Thank you for your visit. Have a great day!")
            save_stock(stock_filename, stock)

if __name__ == "__main__":
    main()
