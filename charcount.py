string=input("Enter the string:")
count=0
for i in range(0,len(string)):
	if string[i]!=' ':
		count=count+1
print("Number of characters in a String:",count)
