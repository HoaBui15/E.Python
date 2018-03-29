#1	binh phuong	
def square(num):		
	return num*num	
number =2		
print(square(number))		
		
#2	chuyen nhiet do / convert temperature
def convert(temp, scale):		
	if scale == "c":	
		return ((temp - 32) * (5.0/9.0))
	elif scale == "f":	
		return (temp*(9.0/5.0) + 32)
temp = int(input("Input temp:" ))		
scale = input("Input scale: ")		
converted = convert(temp,scale)		
print("convert: " + str(converted))		
		
#3		
def oneLine(str):		
	for i in str:	
		print(i)
w =input("Enter word: ")		
print(oneLine(w))		