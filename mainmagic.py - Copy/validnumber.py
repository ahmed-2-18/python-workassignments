import tkinter as tk
#swag one
def validNumberSwag(myNumberValidCheck):
  if int(myNumberValidCheck) >=1 and int(myNumberValidCheck) <=10:
    return True
  else:
    return False
 
# argument: myNumber. Returns True or False








def launchPopup():
  popup = tk.Tk()
  answer = numberEntry.get()
  output = "Hello there " + answer
  #if validNumber(answer) is True, then
  if validNumberSwag(answer)== True:
    output= answer + " " + "is a valid number. Thanks!"
  #     # Set output to be answer "is a valid number. Thanks!"
 
  if validNumberSwag(answer) == False:
    output= answer + " "+ "this is not a valid number to put!"
 
  tk.Label(popup, text=output).pack()




# Write TWO tests of validNumber function. Print your arguments, expected, and actual


# Test ONE
validNumberSwag(11)
print (validNumberSwag(11))
print ("Should be false")

# Test TWO
validNumberSwag(8)
print (validNumberSwag(8))
print ("should be true")


# FINALLY, change the tk.Label below so that the text says “What year were you born?” OR whatever question you choose earlier.


root = tk.Tk()
tk.Label(root, text="On a scale 1-10, what is your swag level.").pack()
numberEntry = tk.Entry(root)
numberEntry.pack()
tk.Button(root, text="Click Me", command=launchPopup).pack()
tk.mainloop()

