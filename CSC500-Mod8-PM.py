class ItemToPurchase:
    def __init__(self):
        self.item_name = "none"
        self.item_price = 0.0
        self.item_quantity = 0

    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        print(f"Item: {self.item_name} Quantity: {self.item_quantity} @ ${self.item_price} = ${total_cost}")

# Item 1
item1 = ItemToPurchase()
print("Item 1")
item1.item_name = input("Enter the item name: ")
item1.item_price = float(input("Enter the item price: "))
item1.item_quantity = int(input("Enter the item quantity: "))

# Item 2
item2 = ItemToPurchase()
print("\nItem 2")
item2.item_name = input("Enter the item name: ")
item2.item_price = float(input("Enter the item price: "))
item2.item_quantity = int(input("Enter the item quantity: "))

# Calculate total cost
total_cost = item1.item_price * item1.item_quantity + item2.item_price * item2.item_quantity

# Output total cost
print("\nTOTAL COST")
item1.print_item_cost()
item2.print_item_cost()
print(f"Total: ${total_cost}")