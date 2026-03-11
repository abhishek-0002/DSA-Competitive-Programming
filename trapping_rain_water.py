'''
Given an array arr[] with non-negative integers representing the height of blocks. If the width of each block is 1, compute how much water can be trapped between the blocks during the rainy season. 

Examples:

Input: arr[] = [3, 0, 1, 0, 4, 0 2]
Output: 10
Explanation: Total water trapped = 0 + 3 + 2 + 3 + 0 + 2 + 0 = 10 units.

Core Idea:
water[i] = min(max height on left, max height on right) - height[i]

So we need:

left[i] → maximum height from 0 → i

right[i] → maximum height from n-1 → i
water += min(left[i], right[i]) - arr[i]
'''

def trap_water(arr):
    n = len(arr)
    
    if n == 0:
        return 0

    # Step 1: Create left max array
    left = [0] * n
    left[0] = arr[0]
    for i in range(1, n):
        left[i] = max(left[i - 1], arr[i])

    # Step 2: Create right max array
    right = [0] * n
    right[n - 1] = arr[n - 1]
    for i in range(n - 2, -1, -1):
        right[i] = max(right[i + 1], arr[i])

    # Step 3: Calculate trapped water
    water = 0
    for i in range(n):
        water += min(left[i], right[i]) - arr[i]

    return water


# Example
arr = [3, 0, 0, 2, 0, 4]
print(trap_water(arr))  # Output: 10

#two poninter approach
'''
Instead of storing left & right max for every index:

Keep two pointers:

left = 0

right = n-1

Maintain:

left_max

right_max

🧠 Core Logic Trick to Remember
Whichever side has smaller height,
that side decides the water.
Because water depends on the minimum of left_max and right_max.

If arr[left] < arr[right]
→ Water is limited by left_max
→ Move left pointer.

Else
→ Water is limited by right_max
→ Move right pointer.
'''
def trap_water(arr):
    n = len(arr)
    left = 0
    right = n - 1
    
    left_max = 0
    right_max = 0
    water = 0

    while left <= right:
        if arr[left] < arr[right]:
            if arr[left] >= left_max:
                left_max = arr[left]
            else:
                water += left_max - arr[left]
            left += 1
        else:
            if arr[right] >= right_max:
                right_max = arr[right]
            else:
                water += right_max - arr[right]
            right -= 1

    return water


# Example
arr = [3, 0, 0, 2, 0, 4]
print(trap_water(arr))  # Output: 10
