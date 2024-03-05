#Emma Moody
#3/5/24
#P2HW2
#Understanding lists and calcuations

#list

mods = []

#grabbing input from user & putting it into list
mods.append(float(input("Enter grade for Module 1: ")))
mods.append(float(input("Enter grade for Module 2: ")))
mods.append(float(input("Enter grade for Module 3: ")))
mods.append(float(input("Enter grade for Module 4: ")))
mods.append(float(input("Enter grade for Module 5: ")))
mods.append(float(input("Enter grade for Module 6: ")))


#results line
print("\n-----------Results------------")

#get the lowest grade/minimum
list_min = min(mods)
print(f"Lowest Grade:     {list_min}")

#get the highest grade/maximum
list_max = max(mods)
print(f"Highest Grade:    {list_max}")

#get the sum of all values in the list
list_sum = sum(mods)
print(f"Sum of Grades:    {list_sum}")

#lengths of the list
list_length = len(mods)
float(list_length)

#average of list
list_average = list_sum / list_length
print(f"Average:          {list_average:.2f}")

#closing lines
print("-----------------------------------")

#:)




