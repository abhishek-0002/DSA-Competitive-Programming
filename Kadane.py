import sys

class Kadane(object):
	def maxsum_subarray(self,arr):
		current_sum=0
		max_sum= -sys.maxsize - 1
		for i in range(len(arr)):
			current_sum+=arr[i]
			if current_sum>max_sum:
				max_sum = current_sum
			if current_sum<0:
				current_sum=0
		return max_sum
arr=[-2, -3, 4, -1, -2, 1, 5, -3]
obj=Kadane()
print(obj.maxsum_subarray(arr))
