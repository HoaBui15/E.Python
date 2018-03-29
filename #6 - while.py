# while
number = 1		
while number < 10:		
	print(number)	
	number+=1	
		
#2		
balance = 1000		
rate = 1.02		
years = 0		
while balance < 5000:		
	balance*=rate	
	years+=1	
print("It takes " + str(years) + " years to reach $5000.")		
#3	
for i in [1,2,3,4,5,6,7,8,9,10]:	
	print(i)
	
#4	
for i in ["John", "Joe", "Marry"]:	
	print(i)
#5	
for i in range(1,11):	
	print(i)