while True:
	n1=int(input('Enter the first number:'))
	n2=int(input("Enter the second number:"))
	op=input('Enter the operation(+,-,*,/):')
	if op=='+':
		print("The Sum is:",n1+n2)
	elif op=='-':
		print("The difference is:",n1-n2)
	elif op=='*':
		print('The product is:',n1*n2)
	elif op=='/':
		if(n2!=0):
			print('The quotient is:',n1/n2)
		else:
			print("Division by Zero is not possible!")
	elif op=='0':
		break;
	else:
		print("Invalid choice!")
	

