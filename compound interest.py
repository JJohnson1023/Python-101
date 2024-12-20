#define the variables that will be used throughout the program
fPrincipleInvestment = float(input("Enter the starting principal: ")) #hope to god they dont put a dollar sign because i dont know how to filter that yet
fInterestRate = float(input("Enter the annual interest rate: "))/100 #<- turn the number into a percentage
iCompounding = int(input("How many times a year is the interest compounded?: "))
iNumberOfPeriods = int(input("How many years will the account earn interest?: "))

#do the math
fFutureValue = fPrincipleInvestment * (1 + (fInterestRate / iCompounding)) ** (iCompounding * iNumberOfPeriods)

#put the math on the screen
print(f"At the end of {iNumberOfPeriods} years, you will have ${fFutureValue:.2f}.")