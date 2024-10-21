def a(m,n):
	print("SUM:",m+n)
def s(m,n):
	print("Difference:",m-n)
def p(m,n):
	print("Product:",m*n)
def q(m,n):
	print("Quotient:",m/n)
def e(m,n):
	print("Power:",m**n)
def calculator(m,n,o):
	if operator=='+':
		a(m,n)
	elif operator=='-':
		s(m,n)
	elif operator=='*':
		p(m,n)
	elif operator=='/':
		q(m,n)
	elif operator=='**':
		e(m,n)
	else:
		print("INVALID!!")
num1=int(input("Enter 1st number:"))
num2=int(input("Enter 2nd number:"))
operator=input("Enter following operator(+,-,*,/,**:)")
calculator(num1,num2,operator)
