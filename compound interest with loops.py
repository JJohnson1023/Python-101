#data validation function
def DataValidation(sQuestion, sForI, bZeroAllowed):
    #sQuestion: the question asked of the user (request an input)
    #sForI: determines whether the output should be a float or an int
    #bZeroAllowed: should zero be considered a valid input?
    bValidInput = False
    while bValidInput == False: #set up the safety net
        try:
            sInput = input(sQuestion) #get user input
            if sForI == "F" or sForI == "f": #determine whether to convert the output to a float or an int
                xOutput = float(sInput)    #"xOutput" can be either a float or an int. not sure how to properly name it.
            else:
                xOutput = int(sInput)

            if bZeroAllowed == True:  # check if zero is allowed.
                if xOutput < 0: #make sure the number is positive
                    print("Please input a positive number")
                else:
                    bValidInput = True

            else:
                if xOutput < 0: #make sure the input is positive
                    print("Please input a positive number.")
                elif xOutput == 0: #make sure the input is greater than zero
                    print("Please input a value greater than zero.")
                else:
                    bValidInput = True

        except ValueError:  #make sure the input is a number
            print("Please input a number.")

    return xOutput

#declare variables
fDeposit = DataValidation("What will be the initial deposit?", "F", False)
fInterestRate = (DataValidation("What is the yearly interest rate? (percentage)", "F", False)/100) /12 #<- convert from percent to decimal, and from yearly to monthly
iMonths = DataValidation("How many months will the interest accrue for?", "I", False)
fGoal = DataValidation("If you have a target balance, what is it? (input \"0\" if you don't.)", "F", True)

#store the original fDeposit value for later use
fDepositOriginal = fDeposit

#do the math for however many months the user has entered, and print it
fInterestTotal = 0
for i in range(1, iMonths+1):
    fInterestTotal = fDeposit * fInterestRate
    fDeposit += fInterestTotal
    print(f"The account's balance on month #{i} will be: ${fDeposit:,.2f}")

if fGoal != 0: #if the user has a target balance
    fInterestTotal = 0
    iGoalMonths = 0

    while fDepositOriginal < fGoal: #determine how long it will take to reach that goal through interest alone
        fInterestTotal = fDepositOriginal * fInterestRate
        fDepositOriginal += fInterestTotal
        iGoalMonths +=1

    #and print it
    print(f"To reach the target balance of ${fGoal:,.2f}, it will take {iGoalMonths} months, with a final balance of ${fDepositOriginal:,.2f}.")