import random 
l=['rock ','paper','scissor']

while True :
    computercount= 0
    yourcount=0
    yourchoice= int(input ('''   
                           GAME START 
                             1. YES 
                             2. NO | EXIT
'''))
    if yourchoice==1:
        for a in range (1,5):
         userinput = int(input('''
                                     1.rock
                                     2.paper
                                     3.scissor                                 
'''))
        if userinput==1:
             yourchoice ="rock"
         
        elif userinput==2:
              yourchoice= "paper"
             
        elif userinput==3:
              yourchoice="scissor "
            
        computerchoice=random.choice(l) 
        if computerchoice==yourchoice:
              print  ("COMPUTER CHOICE ",computerchoice) 
              print  ("YOUR CHOICE ",yourchoice) 
              print  ("GAME DRAW") 
              yourcount=yourcount+1
              computercount =computercount+1 
        elif(yourchoice==""and computerchoice=="rock")or      (yourchoice=="rock"and computerchoice== "scissor")or (yourchoice=="scissor"and computerchoice==""):
              print  ("COMPUTER CHOICE ",computerchoice) 
              print  ("YOUR CHOICE ",yourchoice) 
              print  ("YOU WIN ")
              yourcount=yourcount+1
        else:
              print  ("COMPUTER CHOICE ",computerchoice) 
              print  ("YOUR CHOICE ",yourchoice) 
              print  ("   COMPUTER WIN ")
              computercount=computercount+1
        if  yourcount == computercount :
              
             print  ("FINAL GAME IS DRAW" )
             print  ("COMPUTER CHOICE",computerchoice) 
             print  ("YOUR CHOICE ",yourchoice)
        elif  yourcount<computercount:
            print  ("COMPUTER WIN THE GAME" )
            print  ("COMPUTER CHOICE ",computerchoice) 
            print  ("YOUR CHOICE ",yourchoice)
        else :
            print  ("YOU WIN THE GAME" )
            print  ("COMPUTER CHOICE ",computerchoice) 
            print  ("YOUR CHOICE ",yourchoice)


            
    else :
           break
                  
                    
        
           
