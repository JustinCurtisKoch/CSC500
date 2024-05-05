# Module 3: Critical Thinking Assignment

# Part 1:
# Write a program that calculates the total amount of a meal purchased at a restaurant (total, tip, tax).

# Ask the user to enter the price of the meal
meal_price = float(input("Enter the price of your meal: $"))

# Calculate tip amount (18% of the meal price)
tip = 0.18 * meal_price

# Calculate sales tax amount (7% of the meal price)
sales_tax = 0.07 * meal_price

# Calculate total price (meal price + tip + sales tax)
total_price = meal_price + tip + sales_tax

# Display the amounts and total price
print(f"Tip: ${tip:.2f}")
print(f"Sales Tax: ${sales_tax:.2f}")
print(f"Total Price: ${total_price:.2f}")

# Part 2:
# Write a program that sets an alarm based on a 24 hour clock

# Ask the user for the current time (in hours)
current_time = int(input("Enter the current time (in hours): "))

# Ask the user for the number of hours to wait for the alarm
hours_to_wait = int(input("Enter the number of hours to wait for the alarm: "))

# Calculate the alarm time (current time + hours to wait) % 24
alarm_time = (current_time + hours_to_wait) % 24

# Output the alarm time in a 24-hour clock format
print(f"The alarm will go off at {alarm_time}:00")
