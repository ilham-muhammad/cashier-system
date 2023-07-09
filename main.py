# Project Python - SE/DE Batch 2 Pacmann
# - Task      : Main menu cashier management system
# - Author    : Muhammad Ilham


# import module
from cashier_management_system import Transaction


def main_menu():
    # printing main menu
    print(
        """
            ---------------- Cashier Management System -----------------
            
            Choose transaction options :
            1. Add item
            2. Delete entry
            3. Edit item name
            4. Edit item quantity
            5. Edit item price
            6. Reset transactions
            7. Check order
            8. Check out

            -------------------------------------------------------------
            """
    )

    # initializing choice
    choice = int(input("Chosen option : "))
    if choice == 1:
        transaction.add_item()
    elif choice == 2:
        transaction.delete_item()
    elif choice == 3:
        transaction.update_item_name()
    elif choice == 4:
        transaction.update_item_qty()
    elif choice == 5:
        transaction.update_item_price()
    elif choice == 6:
        transaction.reset_transaction()
    elif choice == 7:
        transaction.check_order()
    elif choice == 8:
        transaction.check_out()
    else:
        print("Invalid options")
        main_menu()


# starting main menu
choice = 0
transaction = Transaction()
while choice != 8:
    main_menu()
