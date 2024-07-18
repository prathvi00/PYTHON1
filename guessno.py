import random 
Cnumber =random.randrange(1,101)
userinput = int (input ("enter your number =="))
if userinput >Cnumber:
    print ("computer guess number ",Cnumber)
    print ("YOUR GUESS NUMBER IS TOO HIGH")
elif userinput < Cnumber:
        print ("computer guess number ",Cnumber)
        print ("YOUR GUESS NUMBER IS TOO LOW")
else:
        print ("computer guess number ",Cnumber)
        print ("YOUR GUESS NUMBER IS EQUAL")

