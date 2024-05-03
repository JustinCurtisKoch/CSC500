
# Create initial array to store the balance/ deposits
deposits = [500]

# Add deposits to the array
deposits.append(1000)  # Next deposit
deposits.append(500)   # Next deposit
deposits.append(750)   # Next deposit
deposits.append(650)   # Next deposit

# Function to calculate interest
def calculate_interest(principal, rate, time):
    interest = principal * rate * time
    return interest

# Calculate total savings
total_savings = sum(deposits)

# Assume an interest rate of 5% per year
interest_rate = 0.05

# Calculate interest earned
total_interest = calculate_interest(total_savings, interest_rate, 1)  # Assuming 1 year

# Print total savings and interest earned
print("Total Savings: $", total_savings)
print("Total Interest Earned: $", total_interest)
