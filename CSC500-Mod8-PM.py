class ItemToPurchase:
    def __init__(self):
        self.item_name = "none"
        self.item_price = 0.0
        self.item_quantity = 0

    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        print(f"Item: {self.item_name} by Quantity: {self.item_quantity} at ${self.item_price} = ${total_cost}")

# Item 1 input
item1 = ItemToPurchase()
print("Item 1")
item1.item_name = input("Enter the item name: ").upper()
item1.item_price = float(input("Enter the item price: "))
item1.item_quantity = int(input("Enter the item quantity: "))

# Item 2 input
item2 = ItemToPurchase()
print("\nItem 2")
item2.item_name = input("Enter the item name: ")
item2.item_price = float(input("Enter the item price: "))
item2.item_quantity = int(input("Enter the item quantity: "))

# Item 3 input
item3 = ItemToPurchase()
print("\nItem 3")
item3.item_name = input("Enter the item name: ")
item3.item_price = float(input("Enter the item price: "))
item3.item_quantity = int(input("Enter the item quantity: "))

# Calculate total cost
total_cost = (item1.item_price * item1.item_quantity) + (item2.item_price * item2.item_quantity) + (item3.item_price * item3.item_quantity)

# Output total cost
print("\nTOTAL COST")
item1.print_item_cost()
item2.print_item_cost()
item3.print_item_cost()
print(f"Total: ${total_cost}")

class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = input("Enter customer's name: ")
        self.current_date = input("Enter today's date: ")
        self.cart_items = []
        print(f"Customer name: {customer_name}")
        print(f"Today's date: {current_date}")

    def add_item(self, item):
        self.cart_items.append(item)

    def remove_item(self, item_name):
        for i in self.cart_items:
            if i.item_name == item_name:
                self.cart_items.remove(i)
                return
        print("Item not found in cart. Nothing removed.")

    def change_item_quantity(self, item_name, new_quantity):
        for item in self.cart_items:
            if item.item_name == item_name:
                item.item_quantity = new_quantity
                return
            print("Item not found in cart. Nothing modified.")

    def modify_item(self, modified_item):
        for item in self.cart_items:
            if item.item_name == modified_item.item_name:
                item.item_price = modified_item.item_price
                item.item_quantity = modified_item.item_quantity
                return
        print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        return sum(item.item_quantity for item in self.cart_items)

    def get_cost_of_cart(self):
        return sum(item.item_price * item.item_quantity for item in self.cart_items)

    def print_total(self):
        if not self.cart_items:
            print("SHOPPING CART IS EMPTY")
            return
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        total_cost = 0
        for item in self.cart_items:
            total_cost += item.item_price * item.item_quantity
            item.print_item_cost()
        print(f"Total: ${total_cost}")

    def print_descriptions(self):
        if not self.cart_items:
            print("SHOPPING CART IS EMPTY")
            return
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            print(f"{item.item_name}: {item.item_quantity} @ ${item.item_price}")

def print_menu():
    print("""
    MENU
    a - Add item to cart
    r - Remove item from cart
    c - Change item quantity
    i - Output items' descriptions
    o - Output shopping cart
    q - Quit
    """)

my_cart = ShoppingCart("Justin Curtis Koch", "May 28, 2024")
print_menu()
while True:
    choice = input("Choose an option: ")
    if choice == 'a':
        item = ItemToPurchase()
        item.item_name = input("Enter item name: ")
        item.item_price = float(input("Enter item price: "))
        item.item_quantity = int(input("Enter item quantity: "))
        my_cart.add_item(item)
    elif choice == 'r':
        item_name = input("Enter item name to remove: ")
        my_cart.remove_item(item_name)
    elif choice == 'c':
        item_name = input("Enter item name to change quantity: ")
        new_quantity = int(input("Enter new quantity: "))
        my_cart.change_item_quantity(item_name, new_quantity)
    elif choice == 'i':
        my_cart.print_descriptions()
    elif choice == 'o':
        my_cart.print_total()
    elif choice == 'q':
        break
    else:
        print("Invalid choice. Please try again.")

customer_name = input("Enter customer's name: ")
current_date = input("Enter today's date: ")
print(f"Customer name: {customer_name}")
print(f"Today's date: {current_date}")

shopping_cart = ShoppingCart(customer_name, current_date)

print("\nADD ITEM TO CART")
item_name = input("Enter the item name: ")
item_description = input("Enter the item description: ")
item_price = float(input("Enter the item price: "))
item_quantity = int(input("Enter the item quantity: "))
new_item = ItemToPurchase(item_name, item_description, item_price, item_quantity)
shopping_cart.add_item(new_item)

print("\nREMOVE ITEM FROM CART")
item_to_remove = input("Enter name of item to remove: ")
shopping_cart.remove_item(item_to_remove)

print("\nCHANGE ITEM QUANTITY")
item_to_change = input("Enter the item name: ")
new_quantity = int(input("Enter the new quantity: "))
shopping_cart.change_item_quantity(item_to_change, new_quantity)