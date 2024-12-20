#this program is held together with hopes and dreams
#nvm i fixed it up

def getFloatInput(intake):
    #intake: the question to be asked of the user
    bValidInput = False     #set up the while loop
    while not bValidInput:
        output = input(intake)    #establish str version of output in case of "n" input
        try:                        #standard data validation, make sure its a number and >0
            if float(output) <= 0:
                print("Please enter a positive number.")
            else:
                bValidInput = True
        except ValueError:
            if output.lower() == "n":   #make sure that "n" isnt filtered out
                return output
            else:                       #otherwise, tell em to put in a number
                print("Please enter a number.")
    return float(output)

def makeList(): #grabs all the inputs and places them into a list
    lPriceList = []
    bContinueLoop = True
    while bContinueLoop:
        fPrice = getFloatInput("Enter the price of the estate, or type \"N\" to conclude the list: ")
        try:
            if fPrice.lower() == "n": #if the user is finished with the list
                bContinueLoop = False #end the sequence
        except AttributeError:       #if the .lower() method fails due to fPrice being a float datatype,
            lPriceList.append(fPrice) #add it to the list
    lPriceList.sort()
    return lPriceList

def printList(lPriceList):
    #lPriceList: the variable of the same name within main()
    for i in range(0, len(lPriceList)):
        print(f"Property #{i+1}: ${lPriceList[i]:,.2f}")

def printMin(lPriceList):
    #lPriceList: the variable of the same name within main()
    print(f"The minimum value is Property #{lPriceList.index(min(lPriceList)) + 1}, with a value of ${min(lPriceList):,.2f}.")

def printMax(lPriceList):
    #lPriceList: the variable of the same name within main()
    print(f"The max value is Property #{lPriceList.index(max(lPriceList)) + 1}, with a value of ${max(lPriceList):,.2f}.")

def getMedian(intake):
    #intake: the list of prices
    if (len(intake) % 2 != 0): #if the length of the list is odd (look scott!! modulus!!!)
        fMedian = intake[len(intake) // 2]
    else: #if it is not odd (therefore it must be even)
        fMedian = (intake[len(intake) // 2] + intake[(len(intake) // 2) - 1]) / 2
    return fMedian

def printMedian(lPriceList):
    #lPriceList: the variable of the same name within main()
    fMedian = getMedian(lPriceList)
    print(f"The median value is ${fMedian:,.2f}.")

def getAverage(lPriceList):
    #lPriceList: the variable of the same name within main()
    fAverage = 0
    for i in range(0, len(lPriceList)):
        fAverage += lPriceList[i]
        if i == len(lPriceList) - 1:
            fAverage /= i+1
    return fAverage

def printAverage(lPriceList):
    #lPriceList: the variable of the same name within main()
    fAverage = getAverage(lPriceList)
    print(f"The average value is ${fAverage:,.2f}.")

def getTotal(lPriceList):
    #lPriceList: the variable of the same name within main()
    fTotal = 0
    for i in range(0, len(lPriceList)):
        fTotal += lPriceList[i]
    return fTotal

def printTotal(lPriceList):
    #lPriceList: the variable of the same name within main()
    fTotal = getTotal(lPriceList)
    print(f"The total value is ${fTotal:,.2f}.")

def getCommission(lPriceList):
    #lPriceList: the variable of the same name within main()
    COMMISSION_RATE = 0.03
    fTotal = getTotal(lPriceList)
    fCommission = fTotal * COMMISSION_RATE
    return fCommission

def printCommission(lPriceList):
    #lPriceList: the variable of the same name within main()
    fCommission = getCommission(lPriceList)
    print(f"The commission value is ${fCommission:,.2f}.")

def main():

    #use a list to store all the user-inputted sales values (while loop, prompt user to enter until there is no more)
    lPriceList = makeList()

    #output each value from the list with dollar sign, commas and .2f
    printList(lPriceList)

    #output the min value with the above formatting
    printMin(lPriceList)

    #and the max value
    printMax(lPriceList)

    #and the median
    printMedian(lPriceList)

    #and the average
    printAverage(lPriceList)

    #and the total
    printTotal(lPriceList)

    #and the commission value
    printCommission(lPriceList)
main()
#*reads the instructions*
#"wow this final project is going to be literally so easy and free, its crazy"
#123 lines, 14 functions and ~8 hours later: