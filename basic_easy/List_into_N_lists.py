class Solution(object):
	def divide_chuks(self,l,n):
		for i in range(0,len(l),n):
			yield l[i:i+n]
	def divide_chuks_2(self,l,n):
		final = [l[i * n:(i + 1) * n] for i in range((len(l) + n - 1) // n )]
	return final  


length_list = int(input("size of list"))
n = int(input("chunk size"))
lst = []

for i in range(length_list):
	element = int(input(f"Enter element {i+1}:"))
	lst.append(element)

obj = Solution()
res = list(obj.divide_chuks(lst,n))
print(res)
