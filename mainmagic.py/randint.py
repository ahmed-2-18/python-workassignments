from random import *



# Section 1: Generate and print the full array...
print("Section 1: Integers from 60 to 120")
# - Create an empty array
myListSection1 = []
# - Using a "for i in range" loop, randomly generate 20 positive integers ranging from 60 to 120 and append them to the array
for i in range(20):
    num = randint(60,120)
    myListSection1.append(num)

# - Print a line that says "FULL ARRAY"
print("FULL ARRAY")
# - Print the full contents of the array using print()
print(myListSection1)


# -=-=-=-=-=-=-=-=-=-=-=-=-

# Section 2: Print the Odd Integers...
print("Section 2: Odd Integers")
# - Create a variable called result and set it to be an empty string ""
result = " "

# - Print a line that says "ODD INTEGERS"
print("ODD INTEGERS")
# - Use a FOR EACH loop to iterate through the array.
for each in myListSection1:
# - If an integer is odd (Hint: use modulus %), then add it to the result string
    if (each % 2) == 1:
        result += str(each) + " And "
    

    
# - Hint: use result = result + str(i) + " & "
 
# - Print result
print(result)
# -=-=-=-=-=-=-=-=-=-=-=-=-

# Section 3: Print the Multiples of 4...
print("Section 3: Multiples of 4")
# - Set result to be an empty string ""
result = " "
# - Use a FOR EACH loop to iterate through the array
for each in myListSection1:
# - If a number is a multiple of 4, add it to result with a " * " separator
    if (each/4):
        result = result + str(each) + " * "

# - Print result
print(result)