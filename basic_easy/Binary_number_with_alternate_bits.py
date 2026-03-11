'''
Given a positive integer, check whether it has alternating bits: namely, 
if two adjacent bits will always have different values.

Example 1:

Input: n = 5
Output: true
Explanation: The binary representation of 5 is: 101
Example 2:

Input: n = 7
Output: false
Explanation: The binary representation of 7 is: 111.
Example 3:

Input: n = 11
Output: false
Explanation: The binary representation of 11 is: 1011.

Intuition:

Simple xor operation helps to check the if the adjacent bits are alternate or not
as
X Y X^Y
0 0 0
0 1 1
1 0 1
1 1 0

To get adjacent bits we need to do right shift of the n then we get adjacent bits 
suppose n = 5 which is 101
n >> 1 = 010
1 0 1
0 1 0
-------
1 1 1
-------

store this 1 1 1 as decimal = 7 
now to check if this 7 has all ones or not we simply add 1
so it becomes 1000 now if we do AND operation 111 & 1000 = 0000
'''
class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        x = n ^ (n >> 1)
        if (x & (x + 1)) == 0:
            return True
        return False