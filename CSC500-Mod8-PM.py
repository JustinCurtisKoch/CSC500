import datetime

class ItemToPurchase:
    def __init__(self, item_name="none", item_descript="none", item_price=0.0, item_quantity=0):
        self.item_name = item_name
        self.item_descript = item_descript
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self):
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.item_price * self.item_quantity}")

class ShoppingCart:
    def __init__(self, customer_name="none", current_date=None,):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item):
        self.cart_items.append(item)

    def remove_item(self, item_name):
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                print(f"Item '{item_name}' removed from cart.")
                return
        print("Item not found in cart. Nothing removed.")

    def modify_item(self, item_to_purchase):
        for item in self.cart_items:
            if item.item_name == item_to_purchase.item_name:
                if item_to_purchase.item_price != 0.0:
                    item.item_price = item_to_purchase.item_price
                if item_to_purchase.item_quantity != 0:
                    item.item_quantity = item_to_purchase.item_quantity
                print(f"Item '{item_to_purchase.item_name}' modified.")
                return
        print("Item not found in cart. Nothing modified.")

    def get_cost_of_cart(self):
        return sum(item.item_price * item.item_quantity for item in self.cart_items)

    def print_descriptions(self):
        if not self.cart_items:
            print("NO ITEMS IN CART")
        else:
            print("Items' Descriptions:")
            for item in self.cart_items:
                print(f"Item name: {item.item_name}")
                print(f"Item description: {item.item_descript}")

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

    def print_menu(self):
        print("\nMENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("m - Modify item in cart")
        print("i - Print descriptions")
        print("o - Print total")
        print("q - Quit")

def main():
    customer_name = input("Enter your name: ")
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    cart = ShoppingCart(customer_name, current_date)

    print(f"\nCart Name: {cart.customer_name}")
    print(f"Date: {cart.current_date}")

    cart.print_menu()
    while True:
        choice = input("Choose an option: ")
        if choice.lower() == 'a':
            item = ItemToPurchase()
            item.item_name = input("Enter item name: ")
            item.item_descript = input("Provide item description: ")
            item.item_price = float(input("Enter item price: "))
            item.item_quantity = int(input("Enter item quantity: "))
            cart.add_item(item)
        elif choice.lower() == 'r':
            item_name = input("Enter the item name to remove: ")
            cart.remove_item(item_name)
        elif choice.lower() == 'm':
            item_name = input("Enter the item name to modify: ")
            new_price = float(input("Enter the new price (or 0 to keep current price): "))
            new_quantity = int(input("Enter the new quantity (or 0 to keep current quantity): "))
            item_to_modify = ItemToPurchase(item_name, new_price, new_quantity)
            cart.modify_item(item_to_modify)
        elif choice.lower() == 'c':
            print(f"Cost of the cart: ${cart.get_cost_of_cart():.2f}")
        elif choice.lower() == 'i':
            cart.print_descriptions()
        elif choice.lower() == 'o':
            cart.print_total()
        elif choice.lower() == 'q':
            print(f"{customer_name}, thank you for shopping!")
            break
        else:
            print("Invalid choice. Please try again.")

    # Run the main function
main()