# Method 1		
import tempconv		
temp = 212		
convTemp = tempconv.ftoc(temp)		
print("The converted temp is " + str(convTemp))		
temp = 0		
conVTemp = tempconv.ctof(temp)		
print("The converted temp is " + str(conVTemp))		
		
# Method 2
from tempconv import ctof		
from tempconv import ftoc		
		
temp = 212		
convTemp = ftoc(temp)		
print("The converted temp is " + str(convTemp))		
temp = 0		
conVTemp = ctof(temp)		
print("The converted temp is " + str(conVTemp))	

#################################################
#import Shape		
from f_shape import Shape
from f_shape import Rectangle
s1 = Shape(4,8)
print(s1)
r1= Rectangle(5,10,6,8)
print(r1)