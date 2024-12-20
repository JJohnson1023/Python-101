import math #this is a surprise tool that will help us later >:)
import random #:)

#define variables that will be used throughout the program
fMercuryGravityScale = 0.38
fVenusGravityScale = 0.91
fTheMoonGravityScale = 0.165
fMarsGravityScale = 0.38
fJupiterGravityScale = 2.34 #this is a gas giant. you are not going to have a good time. (i say that as though you will have any better of a time on mercury or venus)
fSaturnGravityScale = 0.93
fUranusGravityScale = 0.92
fNeptuneGravityScale = 1.12
fPlutoGravityScale = 0.066 #you will live on in our hearts

bAuthorization = False #define a boolean that will be used to prove if you are a human (very important)

iFailCounter = 0 #:)

while(bAuthorization == False): #while you are unauthorized:
    sAuthorization = input(f"ALERT!! Unauthorized user detected! " + #warn the user
                           "Please enter the first 10 digits of pi to prove you are a human." +     #ask the stupidest captcha i have ever come up with
                           "\nformat: \n3.xxxxxxxxxx (the last digit is rounded up)\n")             #give them a chance by showing them what the answer is supposed to look like
    if(sAuthorization == f"{math.pi:.10f}"): #if they correctly input the first 10 digits of pi,
        bAuthorization = True                #let them through
    else:                                    #otherwise,
        iFailCounter += 1                    #add 1 to iFailCounter
        if (iFailCounter >= 3):  #if the user has answered incorrectly 3 or more times,
            sSkipCaptcha = input(f"It appears you have failed to verify your humanity {iFailCounter} times in a row." +
                                 " Would you like to bypass the captcha?\n(Y or N, case sensitive)\n")     #ask the user if they would like mercy
            if (sSkipCaptcha == "Y"):   #if they want mercy
                fMercyCoinFlip = random.random()   #flip a coin
                print("Excuse me while I flip a coin...")
                if(fMercyCoinFlip >= 0.50):       #heads, they win! let them through
                    bAuthorization = True
                    print("Heads! You win! Go on through.")
                else:                             #tails! try again :)
                    bAuthorization = False
                    print("Sorry bud, tails. Better luck next time.")




#done with that mess. now for the real program. thank you for being so patient mr candido

sUserName = input("What is your name?") #ask the name
fUserWeight = float(input("How much do you weigh? (in pounds)")) #ask their weight (and convert it to a float)

#do the math
fMercuryWeight = fUserWeight * fMercuryGravityScale
fVenusWeight = fUserWeight * fVenusGravityScale
fTheMoonWeight = fUserWeight * fTheMoonGravityScale
fMarsWeight = fUserWeight * fMarsGravityScale
fJupiterWeight = fUserWeight * fJupiterGravityScale
fSaturnWeight = fUserWeight * fSaturnGravityScale
fUranusWeight = fUserWeight * fUranusGravityScale
fNeptuneWeight = fUserWeight * fNeptuneGravityScale
fPlutoWeight = fUserWeight * fPlutoGravityScale

#put the math on the screen
print(f"{sUserName} here are your weights on our Solar System's planets:\n" +
      f"Weight on Mercury: {fMercuryWeight:10.2f}\n" +
      f"Weight on Venus:   {fVenusWeight:10.2f}\n" +
      f"Weight on our Moon:{fTheMoonWeight:10.2f}\n" +
      f"Weight on Mars:    {fMarsWeight:10.2f}\n" +
      f"Weight on Jupiter: {fJupiterWeight:10.2f}\n" +
      f"Weight on Saturn:  {fSaturnWeight:10.2f}\n" +
      f"Weight on Uranus:  {fUranusWeight:10.2f}\n" +
      f"Weight on Neptune: {fNeptuneWeight:10.2f}\n" +
      f"Weight on Pluto:   {fPlutoWeight:10.2f}")