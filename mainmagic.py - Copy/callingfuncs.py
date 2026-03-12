# Your work begins on line 23 !!!
# Do NOT edit these first 20 lines of code!

def getFirstVowel(mystring):
    for index, char in enumerate(mystring):
        if char in "aeiou":
            return index
    return 0

def getVowelName(fullName):
    if fullName[0] not in "aeiou":
        return fullName[getFirstVowel(fullName):].lower()
    return fullName.lower()

def playNameGame(fullName):
    vowelName = getVowelName(fullName)
    output = fullName + ", " + fullName + ", bo-B"
    output += vowelName + ". Bonana-fanna fo-F"
    output += vowelName + ". Fee fi mo-M"
    return output + vowelName + ". " + fullName + "!"

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Fill in all 16 blanks below with the correct code.
# Blanks look like this: ???

def test_1_getFirstVowel():
    # call getFirstVowel function, pass argument "Steve",
    # save what it returns in steveText
    steveText = getFirstVowel("Steve")
    # print that variable
    print(steveText)
    # call getFirstVowel function, pass in "Hilliard" as
    # an argument & save what it returns in hillText
    hillText = getFirstVowel("Hilliard")
    # print the variable hillText
    print(hillText)
    # return variable hillText
    return hillText

def test_2_getVowelName():
    # call getVowelName function, pass argument "Christine" &
    # save what it returns in christineText
    christineText = getVowelName("Christine")
    # print the variable christineText
    print(christineText)
    # call getVowelName function, pass in YOUR LAST NAME as
    # an argument & save what it returns in a variable
    myNameAsArguement= getVowelName("Ahmed")
    # print your variable
    print(myNameAsArguement )
    # call getVowelName function, pass argument "Brynn" &
    # save what it returns in brynnText
    brynnText = getVowelName("Brynn")
    # print the variable brynnText
    print( brynnText )
    # return variable brynnText
    return brynnText

def test_3_playNameGame():
    # call playNameGame function, pass argument "Shirley",
    # saves what it returns in variable shirleyText
    shirleyText = playNameGame("Shirley")  
    # print that variable
    print(shirleyText)
    # call playNameGame function, pass in YOUR FIRST NAME as
    # an argument, & save what it returns in a new variable
    myname = playNameGame("Ahmed")
    # print that variable
    print(myname)
    # return your variable
    return myname


# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# You are done!
# Do not edit the code below this line!
print("Test 1 getFirstVowel\nExpected 'Steve' -> 2\nExpected 'Hilliard' -> 1")
test_1_getFirstVowel()
print("Test 2 getVowelName\nExpected 'Christine' -> 'istine'\nExpected 'Name' -> 'ame'\nExpected 'Brynn' -> 'ynn'")
test_2_getVowelName()
print("Test 3 playNameGame")
test_3_playNameGame()