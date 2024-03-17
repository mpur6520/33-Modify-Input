#changed name variable to hold user's input, asks question "Hello! What is your name?" and lets user respond
name = input("Hello! What is your name? ")
print("\nWe want to know if you like progamming!")
print()
#I combined the answer variable and print statement to display as one line - the print statement wasn't needed, as you can type the string you want the question to be into the parentheses of the input. I did this, and assigned the answer to the variable titled answer
answer = input("Do you like programming " + name + "? ")
#for this line, I inputted the name variable as well. This way, it greets using the name inserted in the variable
print("Great, " + name + "! You said " + answer + "!")
print("Let's learn some Python today!")