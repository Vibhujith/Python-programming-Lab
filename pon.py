num=int(input("Enter a Number:"))
sum=0
for i in range(1,num):
	if(num%i==0):
		sum=sum+i
if(sum==num):
	print("the number is perfect")
else:
	print("The number is not perfect")
