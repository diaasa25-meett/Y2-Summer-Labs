import random
tem=[]
odd=0
even=0
for i in range (7):
	tem.append(random.randint(26,40))
days=["sunday","monday","Tuesday","Wednesday","Thursday","friday","Saturday"]
for i in range(7):	
	if i%2==0:
		even+=1
	else:
		odd+=1
