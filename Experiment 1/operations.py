a=int(input('Enter first number:'))
b=int(input("Enter second number:"))
print("Sum is:",a+b)
print("Difference is:",abs(a-b))
print('Product is:',a*b)
try:
	print("Quotient is:",a/b)
except ZeroDivisionError:
	print("Division by Zero not possible!")
if b!=0:
	print("Floor division quotient:",a//b)
else:
	print("Division by Zero not possible!")
try:
	print("Remainder is:",a%b)
except ZeroDivisionError:
	print("Division by Zero not possible!")
print("Exponentation is:",a**b)

