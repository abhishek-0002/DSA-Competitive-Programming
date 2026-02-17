num =29
flag=False

if num>1:
	for i in range(2,num/2):
		if(num%i)==0:
			flag=True
			break


if flag:
	print(num,"is not a prime")
else:
	print(num,"is prime")