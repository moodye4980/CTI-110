'''
#converting datatypes

weekly_rate = input("Enter your weekly pay: ")

weekly_rate = float(weekly_rate)

print("Your weekly pay is", weekly_rate)

#see what the datatype is for a variable
print(type(weekly_rate))

#display bi-weekly pay
print("Every two weeks you make", "$" + str(weekly_rate * 2), "dollars")


'''

#in hw, do not hard code. get values from user. remember to convert to a number datatype

num1 = 3
num2 = 5
print(num1, "*", num2, "=", num1 * num2)

#using exponents

print(num1, "rasied to the power of", num2, "is" num1** num2)