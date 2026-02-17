n_terms=int(input("Enter the number of terms user wants to print?"))
n1=0
n2=1
count=0

if n_terms<0:
	print("please enter the positive integer, the given number is not valid ")

elif n_terms==1:
	print("the fibonacci sequence of the number is ",n1)

else:
	print("The fibonacci sequence of the number is:")
	while count<n_terms:
		print(n1)
		sum=n1+n2
		n1=n2
		n2=sum
		count+=1