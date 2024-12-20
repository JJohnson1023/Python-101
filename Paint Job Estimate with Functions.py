#hmmm today i will take a well deserved break from school
#*checks grades
#coding assignment due at midnight
#welp!!!!!!! :)
#my sheer love for programming will pull me through

import math

def dataValidation(question): #data validation function (make sure it's a number and > 0)
    #question: the question being asked
    bValidInput = False
    while bValidInput == False:
        try:
            intake = input(question)
            if float(intake) <= 0: #not an int, as values that are between 0 and 1 will falsely trigger this if so
                print("Please input a value greater than zero.")
            else:
                bValidInput = True
        except ValueError:
            print("Please enter a number.")
    return intake

def getFloatInput(question): #convert an input to a float
    #intake: the question to be passed to the float conversion function below
    output = float(dataValidation(question))
    return output

def getGallonsOfPaint(fPaintEfficiency, fAreaOfWall): #"return an int of how many gallons are needed,
                                                      # rounded up to the nearest int"
    #fPaintEfficiency: the value of the variable with the same name located in main()
    #fAreaOfWall: the value of the variable with the same name located in main()
    return math.ceil(fAreaOfWall / fPaintEfficiency) #math.ceil will round the float parameter UP to the nearest int
                                                     #(thanks internet) (i hope we're not still under code restrictions)
                                                     #also prof c, if you know a method of doing this without importing
                                                     #an entire library, please let me know in the feedback area

def getLaborHours(fHoursPerGallon, iTotalGallonsRequired): #"returns the total labor hours required to paint the wall
                                                           # as a float"
    #fHoursPerGallon: the value of the variable with the same name located in main()
    #iTotalGallonsRequired: the value of the variable with the same name located in main()
    return fHoursPerGallon * iTotalGallonsRequired #<-- type(float * int) = float

def getLaborCost(fTotalLaborHours, fLaborRate): #returns the total labor cost as a float
    #fTotalLaborHours: the value of the variable with the same name located in main()
    #fLaborRate: the value of the variable with the same name located in main()
    return fTotalLaborHours * fLaborRate

def getPaintCost(iTotalGallonsRequired, fPaintPricePerGallon): #returns the total cost of the paint as a float
    #iTotalGallonsRequired: the value of the variable with the same name located in main()
    #fPaintPricePerGallon: the value of the variable with the same name located in main()
    return iTotalGallonsRequired * fPaintPricePerGallon

def getSalesTax(sState): #returns the tax rate based on what state the job takes place in as a float
    #sState: the data within the string with the same name located in main()
    lDefinedStates =        ["CT", "MA",   "ME",  "NH", "RI", "VT"] #oh my god google makes me such a good programmer-
    lDefinedStatesTaxRates =[0.06, 0.0625, 0.085, 0.0,  0.07, 0.06]#please note, the assignment precisely states that
                                                                   #the tax rate for NH is ".0". I'm interpreting this
                                                                   #literally, hence "0.0".
    for i in range(0, len(lDefinedStates)):             #scan each item within lDefinedStates, and compare them to
        if sState.lower() == lDefinedStates[i].lower(): #sState. if sState is equal to any of these items, return the
            return lDefinedStatesTaxRates[i]            #corresponding tax value. otherwise, return zero.
        else:                                           #also, use the .lower() string method to make the input
            if i == len(lDefinedStates)-1:              #case in-sensitive.
                return 0


def showCostEstimate(fTotalCostOfLabor, fTotalPaintCost, fSalesTaxRate, iTotalGallonsRequired, fTotalLaborHours, sCustomerLastName, bWriteToFile):
#takes all the calculated values, and returns the total cost of the job as a float .2f

    #im sure you get it by now. these function parameters correspond to the variables of the same name within main()
    #bWriteToFile: does the user want the program to write the output to a file?

    if bWriteToFile.lower() == "y":#i know this is technically inefficient, but i believe it would be a best-practice
        bWriteToFile = True        #to convert bWriteToFile to an actual boolean value. in the event that i collaborate
    else:                          #with other programmers on the same project, they would likely expect a variable
        bWriteToFile = False       #with the prefix of "b" to have a value of True / False rather than "y" / "n".
                                   #it simply prevents issues that could come up. correct me if i'm wrong, though

    output = (f"Total cost for the job:    ${(fTotalCostOfLabor + fTotalPaintCost) * (1+fSalesTaxRate):.2f}\n" +
              f"Required gallons of paint:  {iTotalGallonsRequired}\n" +
              f"Total hours of labor:       {fTotalLaborHours:.1f}\n" +
              f"Total cost of paint:       ${fTotalPaintCost:.2f}\n" +
              f"Total cost of labor:       ${fTotalCostOfLabor:.2f}\n" +
              f"Total Taxes:               ${(fTotalCostOfLabor + fTotalPaintCost) * fSalesTaxRate:.2f}")
    print(output)


    if bWriteToFile == True:
        file = open(f"{sCustomerLastName}_PaintJobOutput.txt", "w")
        file.write(output)
        file.close()



def main():
    #ask sqft of wall
    fAreaOfWall = getFloatInput("What is the area of the wall in square feet?: ")

    #ask paint price per gallon
    fPaintPricePerGallon = getFloatInput("What is the cost of each gallon of paint?: ")

    #ask how many sqft can you get out of each gallon of paint
    fPaintEfficiency = getFloatInput("How many square feet can you paint with a single gallon?: ")

    #ask how many labor hours per gallon
    fHoursPerGallon = getFloatInput("How many hours does it take to use up a whole gallon of paint?: ")

    #ask how much the labor will cost per hour
    fLaborRate = getFloatInput("What is the cost per hour for the labor?: ")

    #ask which US state the job will be taking place in
    sState = input("What state will the job be taking place in? (Use the two-letter abbreviation)" +
                   " (*not* case sensitive!!): ")

    #ask the customer's last name
    sCustomerLastName = input("What is the customer's last name?: ")

#--------------------------------------------------------------------------------#
    iTotalGallonsRequired = getGallonsOfPaint(fPaintEfficiency, fAreaOfWall)

    fTotalLaborHours = getLaborHours(fHoursPerGallon, iTotalGallonsRequired)

    fTotalCostOfLabor = getLaborCost(fTotalLaborHours, fLaborRate)

    fTotalPaintCost = getPaintCost(iTotalGallonsRequired, fPaintPricePerGallon)

    fSalesTaxRate = getSalesTax(sState)

    showCostEstimate(fTotalCostOfLabor, fTotalPaintCost, fSalesTaxRate, iTotalGallonsRequired, fTotalLaborHours, sCustomerLastName, input("Would you like to write the output to a file? (Y/N): "))

#--------------------------------------------------------------------------------#

    #heres some leftover lines from testing / debugging. i left them in so you can de-comment them if it makes grading
    #any easier. if de-commented, they will print the value of every variable once the main program is finished.
'''
    print(f"fAreaOfWall = {fAreaOfWall}")
    print(f"fPaintPricePerGallon = {fPaintPricePerGallon}")
    print(f"fPaintEfficiency = {fPaintEfficiency}")
    print(f"fHoursPerGallon = {fHoursPerGallon}")
    print(f"fLaborRate = {fLaborRate}")
    print(f"sState = {sState}")
    print(f"fSalesTaxRate = {fSalesTaxRate}")
    print(f"sCustomerLastName = {sCustomerLastName}")
    print(f"iTotalGallonsRequired = {iTotalGallonsRequired} ({fAreaOfWall} / {fPaintEfficiency}, rounded up to the " +
                                    f"nearest int that is >= itself, and converted to int)")
    print(f"fTotalLaborHours = {fTotalLaborHours} ({iTotalGallonsRequired} * {fHoursPerGallon})")
    print(f"fTotalCostOfLabor = {fTotalCostOfLabor} ({fTotalLaborHours} * {fLaborRate})")
    print(f"fTotalPaintCost = {fTotalPaintCost} ({iTotalGallonsRequired} * {fPaintPricePerGallon})")
'''


main()
#this was actually very fun. i thought it would be stressful since i found out that this was due at midnight at 6pm of
#the due date, but i tossed on some music and had a great time. i learned how to do a lot of stuff i couldn't before :)
#(it also helps that i already did about 30% of this assignment previously when i had spare time. lol)
#total time taken: ~4-5 hours.