#hello prof c.
#since i only caught the fact that this assignment is due at midnight today at 7pm,
#i thought it might be fun to time myself with LiveSplit to see just how fast i can crank this program out.
#ill put the final time at the bottom of the program.
#time starts after i hit enter to leave this line:

print("Welcome to my temperature converter!")
#wtf is hungarian notation

#ask the user for necessary inputs
fInputTemp = float(input("Enter a temperature: "))
sCorF = input("Is the temp F for Fahrenheit, or C for Celsius?: ")

#the input is celsius
if sCorF == "C" or sCorF == "c":
    if fInputTemp > 100:                                            #filter out >boiling
        print("The temperature cannot exceed 100C or 212F.")
    else:
        fOutputTemp = ((5.0/9.0) * fInputTemp + 32)                 #do the math
        print(f"The Fahrenheit equivalent is: {fOutputTemp:.1f}")   #put the math on the screen

#the input is fahrenheit
elif sCorF == "F" or sCorF == "f":
    if fInputTemp > 212:                                            #filter out >boiling
        print("The temperature cannot exceed 100C or 212F.")
    else:
        fOutputTemp = ((5.0/9) * fInputTemp - 32)                   #do the math
        print(f"The Celsius equivalent is: {fOutputTemp:.1f}")      #put the math on the screen

#the user is a smartass
else:
    print("Enter a C or F.")








#first draft finished at 19:36
#c works, f doesnt
#second draft, 21:04
#21:50, tested and results are completely satisfactory.
#23:13, code cleaned up, made as readable as possible, and additional comments added