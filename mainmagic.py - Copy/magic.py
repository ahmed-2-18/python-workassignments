def magicTrick():
    # REMINDER: All your code MUST be indented by 4 spaces
    # Use the print function to say "Hello World"
    print("hello world" )
    # Create variable named magicNumber & set it to ANY number you like
    magicNumber = 123
    # Print magicNumber. I will do this step for you
    print(magicNumber)
    # Create variable named stepOne & set it to magicNumber multiplied by 2
    stepOne = (magicNumber*2)
    # Print stepOne
    print(stepOne)
    # Create variable named stepTwo & set it to stepOne plus 10
    stepTwo = (stepOne+10)
    # Print stepTwo
    print(stepTwo)
    # Create variable named stepThree & set it to stepTwo divided by 2
    stepThree = (stepTwo/2)
    # Print stepThree
    print(stepThree)
    # Create variable named stepFour & set it to stepThree minus magicNumber
    stepFour = (stepThree-magicNumber)
    # Print "The next number should be 5.0"
    print("the next number should be 5.0")
    # Print stepFour
    print(stepFour)
    # use the str() function to convert the stepFour variable to a String
    stepFour = str(stepFour)
    # YOU SHOULD BE DONE! Press the Run button. If no errors, then Submit
    return stepFour

result = magicTrick()
print("\nExpected : 5.0 \nYour code: " + result)