def fact(n):
	if(n==1 or n==0):
		return 1
	else:
		return n*fact(n-1)
num=5
print("factorial of ",num,"is ",fact(num))
