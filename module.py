def sum (a,b ):
    c=a+b 
    return c
                    #   this function file name can use in another file in file name 
def mul (a,b):
    c=a*b 
    return c 

# if we type in other file to use this function so

import module as m 
print (m.sum (10,20))
                        #   this type we can use any module one by one



from module import *
print (sum(10,20))
                    #  this mean is * count all for function and we can use these name only 