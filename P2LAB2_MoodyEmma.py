#Emma Moody
#2/27/24
#P2LAB2  Math expressions and f-strings


#get input from user
num1 = float(input("Enter a float: "))
num2 = float(input("Enter a float: "))
num3 = float(input("Enter a float: "))
num4 = float(input("Enter a float: "))

#calculate the product of the variables
product = num1 * num2 * num3 * num4

#calculate average
average = (num1 + num2 + num3 + num4) / 4

#display info to user
print(f"The product is: {product:.0f}")
print(f"The average is: {average:.0f}")

#disply info to user
print(f"The product is: {product:.3f}")
print(f"The average is: {average:.3f}")
