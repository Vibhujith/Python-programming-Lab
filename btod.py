binary=input("Enter a Binary Number:")
binary_no=binary[2:]
binary_no=binary[::-1]
decimal_no=0
for i in range(len(binary_no)):
	digit=int(binary_no[i])
	power=2**i
	result=digit*power
	decimal_no+=result
print(decimal_no)
