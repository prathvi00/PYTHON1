#         *********CALCULATOR*********

num1 = int(input ("enter your first number="))
num2 = int (input ("enter your second number= "))
opertor = input ("enter your opertor= ")
if (opertor == "+"):
    print (num1+num2 )
elif (opertor=="-"):
    print (num1-num2)
elif (opertor== "*"):
    print (num1*num2)
elif (opertor=="/"):
    print (num1/num2)
else:
    print ("invalid opertor ")