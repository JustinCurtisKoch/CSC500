# Module 5: Critical Thinking Assignment

# Part 1: Average Rainfall
total_years = int(input("Enter the number of years recored: "))
total_months = total_years * 12
total_rainfall = 0

for year in range(1, total_years + 1):
    for month in range(1, 13):
        rainfall = float(input(f"Enter the inches of rainfall for Year {year}, Month {month}: "))
        total_rainfall += rainfall

average_rainfall = total_rainfall / total_months

print("Number of months:", total_months)
print("Total inches of rainfall:", total_rainfall)
print("Average rainfall per month:", average_rainfall)


# Part 2: CSU Global Book Club 
books_purchased = int(input("Enter the number of books purchased this month: "))
points_awarded = 0

if books_purchased <= 1:
    points_awarded = 0
elif books_purchased in range(2, 4):
    points_awarded = 5
elif books_purchased in range(4, 6):
    points_awarded = 15
elif books_purchased in range(6, 8):
    points_awarded = 30
elif books_purchased >= 8:
    points_awarded = 60

print("Points awarded:", points_awarded)