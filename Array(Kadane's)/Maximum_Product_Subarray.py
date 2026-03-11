'''
Given an array arr[] that contains positive and negative integers (may contain 0 as well). 
Find the maximum product that we can get in a subarray of arr[].

Note: It is guaranteed that the answer fits in a 32-bit integer.

Examples

Input: arr[] = [-2, 6, -3, -10, 0, 2]
Output: 180
Explanation: The subarray with maximum product is [6, -3, -10] 
with product = 6 * (-3) * (-10) = 180.

'''
def maxProduct(arr):
    max_prod = arr[0]
    min_prod = arr[0]
    result = arr[0]

    for i in range(1, len(arr)):
        num = arr[i]

        if num < 0:
            max_prod, min_prod = min_prod, max_prod

        max_prod = max(num, max_prod * num)
        min_prod = min(num, min_prod * num)

        result = max(result, max_prod)

    return result