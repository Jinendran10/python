s=input('enter a String:')
c=0
for i in s:
	c+=1
print("the total no.of characters are:",c)
print("Upper case letters:",s.upper())
print("Lower case letters:",s.lower())
st=s.replace(' ','_')
print("New String:",st)
if 'Python' in s:
	print("The word 'Python' is present!")
else:
	print("The word 'Python' is not present!")
