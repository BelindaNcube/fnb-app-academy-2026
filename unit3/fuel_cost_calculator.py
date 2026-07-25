# Unit 3 Challenge: The South African Fuel Cost Calculator

# With petrol prices shifting, drivers want to calculate travel costs. Create a quick calculator:
#
# 1. Ask the user how many kilometers they want to drive.
# 2. Ask them for the current petrol price per liter (this can be a decimal, like R22.45).
# 3. Assume their car uses exactly 1 liter of fuel for every 10 kilometers driven.
# (Formula: liters_needed = kilometers / 10).
# 4. Calculate the total cost (liters_needed * petrol_price).
# 5. Use type casting to ensure your numbers work, and use round() to format the
# final cost to 2 decimal places.

kilometers = float(input("Enter the number of kilometers you want to drive: "))
petrol_price = float(input("Enter the current petrol price per liter (R): "))

liters_needed = kilometers / 10
total_cost = round(liters_needed * petrol_price, 2)

print(f"\nDistance: {kilometers} km")
print(f"Fuel needed: {liters_needed} liters")
print(f"Petrol price: R{petrol_price} per liter")
print(f"Total cost: R{total_cost}")