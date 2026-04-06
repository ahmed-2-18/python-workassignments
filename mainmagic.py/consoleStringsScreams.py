print("Enter your first name:")
userName = input()
print("Hello!" + userName)

print("Length is")

print(len(userName))

print("Starts with")

print(userName[0])

print("Ends with")

print(userName[-1])

print("Enter your last name:")
userNameLast = input()

print("Length is")

print(len(userNameLast))

print("Starts with")
print(userNameLast[0])

print("Ends with")

# Print the full name (Your full name is Steve Jobs).

print("Your full name is" + userName + " " + userNameLast)

# Print your nick name is then the first 2 letters of your last name plus the first 2 letters of your last name. Read this article about how to slice a string in Python.
nickName = userNameLast[:2] + userNameLast[:2]
print("Your nickname is " + nickName)
# Finally, scream! Create a variable named myScream that contains empty string. Make a loop that repeats for the length of the first name + the length of the second name, concatenating an "A" to myScream each repetition. After the loop, concatenate an "!" and print it.
myScream = " "
for i in range(len(userName) + len(userNameLast)):
    myScream += "A"
    myScream += "!"
print(myScream)