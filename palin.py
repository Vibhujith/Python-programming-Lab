def palin(n):
	rev=n[::-1]
	if n==rev:
		return True
	else:
		return False
n=input("Enter a string:")
result=palin(n)
if result==True:
	print("PALINDROME")
else:
	print("NOT PALINDROME")
	
