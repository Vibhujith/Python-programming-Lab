def sum_of_first_n(n):
	sum=0
	for i in range(1,n+1):
		sum=sum+i
		i=i+1
	return sum
n=int(input("Enter the Number:"))
result=sum_of_first_n(n)
print("sum of  first",n,"number are:",result)

