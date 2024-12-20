#lets have some fun! >:)
#ill try idiot-proofing this code and implementing a function, just for fun


#ask for the name of the student
sStudentName = input("What is the name of the student?: ")


#define a subroutine so that our code looks sexy (this took way too long)
def GetInput(index):
    #index will (effectively) count how many times this function has been called
    iTest = -1
    while iTest < 0:
        try:
            iTest = int(input(f"What is the score of test #{index}?: "))
            if iTest < 0: #idiot proofing
                print("Please enter a positive number.")
        except ValueError: #more idiot proofing
            print(f"Please enter a number.")
    return iTest


#ask for the test scores
iTest1 = GetInput(1) #<-- these numbers are what "index" from our function will be assigned to
iTest2 = GetInput(2)
iTest3 = GetInput(3)
iTest4 = GetInput(4)


#ask if the user would like to drop the lowest test score
iIdiotTest = 0 #guess what this variable is used for
while iIdiotTest == 0:
    sDropLowestTest = input("Would you like to drop the lowest test score? (Y/N): ")
    if sDropLowestTest == "Y" or sDropLowestTest == "y":
        bDropLowestTest = True
        iIdiotTest = 1
    elif sDropLowestTest == "N" or sDropLowestTest == "n":
        bDropLowestTest = False
        iIdiotTest = 1
    else:
        print("Please answer Yes or No. (Y/N).")
        #you failed the idiot test........


iTotalTests = 4 #<-- will be used in the averaging calculation

if bDropLowestTest == True:

    iTotalTests = 3

    #find the lowest test score by doing a single pass of a simple comparison sort
    iPlaceholderSlot = 0
    if iTest1 < iTest2:              #if test 1 is less than test 2
        iPlaceholderSlot = iTest1    #store the value of test 1 so that it isnt lost
        iTest1 = iTest2              #replace test 1 with test 2
        iTest2 = iPlaceholderSlot    #replace test 2 with test 1's original value

    if iTest2 < iTest3:              #repeat, all the way through
        iPlaceholderSlot = iTest2
        iTest2 = iTest3
        iTest3 = iPlaceholderSlot

    if iTest3 < iTest4:              #until eventually,
        iPlaceholderSlot = iTest3
        iTest3 = iTest4              #like magic,
        iTest4 = iPlaceholderSlot    #iTest4 will now be the least value no matter what.

    iTest4 = 0                       #and we turn it to zero, making it no longer a factor in the averaging calculation


#71 lines in, and we finally get to do the math!!!!
fAverageScore = (iTest1 + iTest2 + iTest3 + iTest4) / iTotalTests


#oh dear god i have to put that table into this program....... im already 90 minutes in, lets make it 90 more!!!!
#letter grade shenanigans
if fAverageScore >= 97:
    sLetterGrade = "A+"
elif fAverageScore >= 94:
    sLetterGrade = "A"
elif fAverageScore >= 90:
    sLetterGrade = "A-"
elif fAverageScore >= 87:
    sLetterGrade = "B+"
elif fAverageScore >= 84:
    sLetterGrade = "B"
elif fAverageScore >= 80:
    sLetterGrade = "B-"
elif fAverageScore >= 77: #more if-elses than yanderedev.
    sLetterGrade = "C+"
elif fAverageScore >= 74:
    sLetterGrade = "C"
elif fAverageScore >= 70:
    sLetterGrade = "C-"
elif fAverageScore >= 67:
    sLetterGrade = "D+"
elif fAverageScore >= 64:
    sLetterGrade = "D"
elif fAverageScore >= 60:
    sLetterGrade = "D-"   #GIVE IT UP FOR LINE 100!!!!! jeez, were finally getting to the challenging stuff, huh?
else:
    #sLetterGrade = "Bro you fucked up..."
    sLetterGrade = "F"

print(f"The test average for {sStudentName} is {fAverageScore:.1f}.\n"
      f"The letter grade is a {sLetterGrade}.")

#in total, this took me about 2 hours. im glad were finally getting to the challenging stuff