#Emma Moody
#2/22/24
#P1HW2
#input and output, values and math with python

print("This programm calculates and displats travel expenses")

budget = float(input("\nEnter Budget: "))

location = input("\nEnter your travel destination: ")

fuel = float(input("\nHow much do you think you will spend on gas? "))

accomodation = float(input("\nAproximately, how much will you need for accomodation/hotel? "))

food = float(input("\nLast, how much do you need for food? "))

print("\n----------Travel Expenses-----------")
print("Location: " + location)
print("Initial Budget: ", budget)

print("\nFuel: ", fuel)
print("Accomodation: ", accomodation)
print("Food: ", food)

expenses = fuel + accomodation + food

print("\nRemaining Balance: ", budget - expenses)
