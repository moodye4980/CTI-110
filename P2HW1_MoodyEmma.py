#Emma Moody
#2/29/24
#P2HW1
#Types of data and calucations

print("This program calculates and displats travel expenses")
budget = float(input("\nEnter Budget : "))
destination = input("\nEnter your travel destination: ")
gas = float(input("\nHow much do you think you will spend on gas? "))
accomodations = float(input("\nApproximately, how much will you need for accomodation/hotel? "))
food = float(input("\nApproximately, how much do you need for food? "))

print("\n-----------Travel Expenses------------")
print("Location:          " + destination)
print(f"Initial Budget:    ${budget:.2f}")
print(f"Fuel:              ${gas:.2f}")
print(f"Accomodations:     ${accomodations:.2f}")
print(f"Food:              ${food:.2f}")
print("--------------------------------------")

expenses = gas + accomodations + food

print(f"Remaining Balance: ${budget - expenses:.2f}")
