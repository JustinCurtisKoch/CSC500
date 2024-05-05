# Module 1: Critical Thinking Assignment

# Part 1:
# Write a Python program to find the addition and subtraction of two numbers.

# Input from user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Addition
sum_result = num1 + num2
print("The sum of", num1, "and", num2, "is:", sum_result)

# Subtraction
sub_result = num1 - num2
print("The difference of", num1, "and", num2, "is:", sub_result)


# Part 2:
# Write a Python program to find the multiplication and division of two numbers.

# Input from user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Multiplication
mul_result = num1 * num2
print("The product of", num1, "and", num2, "is:", mul_result)

# Division
if num2 != 0:
    div_result = num1 / num2
    print("The division of", num1, "by", num2, "is:", div_result)
else:
    print("Cannot divide by zero.")
