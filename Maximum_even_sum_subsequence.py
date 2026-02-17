class Solution(object):
    
    def getmaximumEvenSum(self,val):
        INT_MIN = -100000000
        n =len(val)
        pos_sum = 0
        for i in range(n):  
            if (val[i] > 0):  
                pos_sum += val[i]  
      
        # If sum is even, it is our answer  
        if (pos_sum % 2 == 0):  
            return pos_sum  
      
        # Traverse the array to find the  
        # maximum sum by adding a positive  
        # odd or subtracting a negative odd  
        ans = INT_MIN;  
        for i in range(n): 
            if (val[i] % 2 != 0): 
                if (val[i] > 0):  
                    ans = max(ans, pos_sum - val[i]) 
                else: 
                    ans = max(ans, pos_sum + val[i]) 
        return ans 
obj = Solution()
lst =[-1,-2,-1,8,7]
res = obj.getmaximumEvenSum(lst)
print(res)
