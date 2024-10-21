list1=[]
n=int(input("Enter no. of elements:"))
for i in range(0,n):
	element=input("Enter the element:")
	list1.append(element)
max1=len(list1[0])
temp=list1[0]
for i in list1:
	if(len(i)>max1):
		max1=len(i)
		temp=i
print("The word with the longest length is:",temp,"and length is",max1)
	
	
