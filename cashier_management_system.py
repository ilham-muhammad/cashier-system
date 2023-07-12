# Project Python - SE/DE Batch 2 Pacmann
# - Task      : Create a cashier management system
# - Author    : Muhammad Ilham


# import module
from tabulate import tabulate
from sqlalchemy import create_engine, text


# Defining class : user transaction to add item, remove, or change during transaction
class Transaction:
    """
    A class to make a purchase for each transaction, attributes were designed as list, each entry will fill all of the list element based on their entry index

    attribute:
        - item_name_list = inputed items, element's index corespond to other field attribute
        - quantity_list = quantity of items being purchased
        - unit_price_list = price per items being purchased
        - total_price_list = quantity * price per item
        - discount_list = discount factor for each item based on total price per item
        - discounted_price_list = final price per item after discounted
        - table = dictionary format for all attributes

    method:
        - add_item = to add item & its attributes
        - update_item_name = replace name of added item
        - update_item_qty = replace quantity of added item
        - update_item_price = replace unit price of added item
        - delete_item = delete a single entry consists of name, quantity, & price
        - reset_transaction = empty the basket & deleting all of entry
        - check_order = checking negative value data & showing data in table format
        - check_out = shows final purchase price, send entry to database, & finish purchasing
    """

    # defining initial attributes as list to accomodate index based transaction
    def __init__(self):
        self.item_name_list = []
        self.quantity_list = []
        self.unit_price_list = []
        self.total_price_list = []
        self.discount_list = []
        self.discounted_price_list = []
        self.table = {}

    # method to add item, quantity, & its price into transaction list
    def add_item(self):
        # input data & cast to designated datatype
        item_name, quantity, unit_price = input(
            "Add item, quantity, & its unit price (format: <name>, <qty>, <price>) :\n"
        ).split(",")
        quantity = int(quantity)
        unit_price = int(unit_price)

        self.item_name_list.append(item_name)
        self.quantity_list.append(quantity)
        self.unit_price_list.append(unit_price)

    # method to update/replace item name
    def update_item_name(self):
        item_name, updated_name = input(
            "Replace item name (format: <old name>, <new name>) :\n"
        ).split(",")
        self.item_name_list = [
            updated_name for name in self.item_name_list if name == item_name
        ]

    # method to update/replace a quantity
    def update_item_qty(self):
        item_name, updated_qty = input(
            "Replace quantity based on item name (format: <item name>, <new qty>) :\n"
        ).split(",")
        updated_qty = int(updated_qty)

        index = self.item_name_list.index(item_name)
        self.quantity_list[index] = updated_qty

    # method to update/replace a price
    def update_item_price(self):
        item_name, updated_price = input(
            "Replace price based on item name (format: <item name>, <new price>) :\n"
        ).split(",")
        updated_price = int(updated_price)

        index = self.item_name_list.index(item_name)
        self.unit_price_list[index] = updated_price

    # method to delete an entry/row based on item name
    def delete_item(self):
        item_name = input("Delete entry based on item name : ")
        index = self.item_name_list.index(item_name)
        self.item_name_list.pop(index)
        self.quantity_list.pop(index)
        self.unit_price_list.pop(index)
        self.total_price_list.pop(index)

    # method to reset all transaction item list
    def reset_transaction(self):
        self.item_name_list = []
        self.quantity_list = []
        self.unit_price_list = []
        print("The purchase has been reset")

    # method to check transaction list & data error
    def check_order(self):
        # Check inputed data
        for qty, price in zip(self.quantity_list, self.unit_price_list):
            if qty <= 0 or price <= 0:
                raise Exception("Wrong data detected")
                break
        print("Data is correct")

        # creating total price per item based on unit price * quantity
        self.total_price_list = [
            qty * unit_price
            for qty, unit_price in zip(self.quantity_list, self.unit_price_list)
        ]

        # creating table dictionary
        self.table = {
            "No": [row for row in range(1, len(self.item_name_list) + 1)],
            "Item Name": self.item_name_list,
            "Item Quantity": self.quantity_list,
            "Unit Price": self.unit_price_list,
            "Total Price": self.total_price_list,
        }

        # showing transaction in table format
        print(tabulate(self.table, headers="keys", tablefmt="github"))

    # method to check out & adding discount based on total price transaction
    def check_out(self):
        # adding discount rule on total price per item, while updating discounted price
        for price in self.total_price_list:
            if price > 500_000:  # gets 7% discount
                self.discount_list.append(price * 0.07)
                self.discounted_price_list.append(price * 0.93)
            elif price > 300_000:  # gets 6% discount
                self.discount_list.append(price * 0.06)
                self.discounted_price_list.append(price * 0.94)
            elif price > 200_000:  # gets 5% discount
                self.discount_list.append(price * 0.05)
                self.discounted_price_list.append(price * 0.95)
            else:
                pass

        # showing transaction & adding discount in table format
        self.table["Discount"] = self.discount_list
        self.table["Discounted Price"] = self.discounted_price_list
        print(tabulate(self.table, headers="keys", tablefmt="github"))

        # total transaction
        all_item_price = sum(self.discounted_price_list)
        print("Your total purchase : ", all_item_price)
        print("Thank you for your purchase.")

        # export transaction data to database
        engine = create_engine("sqlite:///example.db")
        conn = engine.connect()

        # create table structure & export querry
        query = text(
            """
                    CREATE TABLE transaction(
                        no_id INT PRIMARY KEY, 
                        item_name VARCHAR(255), 
                        item_qty INT, 
                        unit_price NUMERIC,
                        total_price NUMERIC, 
                        discount NUMERIC,
                        discounted_price NUMERIC
                    )
                    """
        )
        conn.execute(query)

        # create querry to insert data
        query = text(
            """
                    INSERT INTO transaction(no_id, item_name, item_qty, unit_price, total_price, discount, discounted_price)
                    VALUES (:no_id, :item_name, :item_qty, :unit_price, :total_price, :discount, :discounted_price)
                    """
        )
        conn.execute(
            query,
            no_id=self.table["No"],
            item_name=self.table["Item Name"],
            item_qty=self.table["Item Quantity"],
            unit_price=self.table["Unit Price"],
            total_price=self.table["Total Price"],
            discount=self.table["Discount"],
            discounted_price=self.table["Discounted Price"],
        )
        conn.close()
