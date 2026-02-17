num=int(input("Enter the number you want to check"))

length=len(str(num))

sum=0

temp=num

while temp>0:
	digit = temp % 10
	sum = sum + digit**length
	temp = temp//10

if num==sum:
	print(num,'is an armstrong number ')
else:
	print(num,'is not an armstrong number')