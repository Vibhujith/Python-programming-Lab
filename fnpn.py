from math import sqrt
n=int(input("Enter the range:"))
count=0
num=2
print("first",n,"prime numbers are:")
while(count<n):
	is_prime=True
	for i in range(2,int(sqrt(num))+1):
		if(num%i==0):
			is_prime=False
			break
	if is_prime:
		print(num,end="\t")
		count=count+1
	num=num+1
