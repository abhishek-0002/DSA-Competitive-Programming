'''
Given a garden with n flowers planted in a row, that is represented by an array arr[], 
where arr[i] denotes the height of the ith flower.You will water them for k days. 
In one day you can water w continuous flowers. Whenever you water a flower its height 
increases by 1 unit. You have to maximize the minimum height of all flowers after  
k days of watering.

Examples:

Input: arr[] = [2, 3, 4, 5, 1], k = 2, w = 2
Output: 2
Explanation: The minimum height after watering is 2.
Day 1: Water the last two flowers -> arr becomes [2, 3, 4, 6, 2]
Day 2: Water the last two flowers -> arr becomes [2, 3, 4, 7, 3]
Input: arr[] = [5, 8], k = 5, w = 1

Output: 9
Explanation: The minimum height after watering is 9.
Day 1 - Day 4: Water the first flower -> arr becomes [9, 8]
Day 5: Water the second flower -> arr becomes [9, 9]

Intuition:
Step 1
Guess a minimum height (say X)

Step 2
Check if we can make every flower ≥ X in ≤ k days

If yes → try bigger X
If no → try smaller X

This is why we use binary search.

When checking if we can make height ≥ X:

We go left to right.

If at index i:

arr[i] < X


Then we are forced to water starting at i,
otherwise this flower will remain below X forever.

So we:

Calculate how much it needs

Use that many watering operations

That automatically increases next w flowers too

Then continue forward.


How do we choose (take) X?

As X lies between arr(min) = low
and high = max(arr) + k

we pick the x by binary search 

But you may ask why we need to use Binary search ?
As we dont Know the value of X but it will be low <= X <= high
And if we choose X say X = 4  is possible to make all the flowers 4 then 2, 3, 4 are also
possible.
Say we have  arr [1,2,1,2,1]
k=2, w=2
low = 1, high = 2+2 = 4
mid = (1+4)/2 = 2
Now for suppose X = 2,
then at index 0,
arr[0]=1 
to make 1->2, diff = 1, water_used = 1
new array = [2,3,1,2,1]
index  1,
arr[1]=3
3>=2 

index 2,
arr[2]=1
diff = 1, water_used = 2
arr [2,3,2,3,1]

index 3
arr[3]=3
3>=2

index 4
arr[4]=1
water_used = k
Not possible to make all the minimum flowers to height X=2 

'''


class Solution():
    def maxMinHeight(self, arr, k, w):
        # code here
        n = len(arr)
        def can_make(target):
            temp = arr[:]  # copy original heights
            water_used = 0
            added = [0] * (n + 1)
            curr_add = 0
        
            for i in range(n):
                curr_add += added[i]
                if temp[i] + curr_add < target:
                    diff = target - (temp[i] + curr_add)
                    water_used += diff
                    
                    if water_used > k:
                        return False
                    
                    curr_add += diff
                    if i + w < n:
                        added[i + w] -= diff
        
            return True

        low = min(arr)
        high = max(arr) + k
        ans = low
    
        while low <= high:
            mid = (low + high) // 2
            if can_make(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
    
        return ans   
        