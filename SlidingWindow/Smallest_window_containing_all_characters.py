'''
Given two strings s and p. Find the smallest substring in s consisting of all the 
characters (including duplicates) of the string p. Return empty string in case no 
such substring is present. If there are multiple such substring of the same length found, 
return the one with the least starting index.

Examples:

Input: s = "timetopractice", p = "toc"
Output: "toprac"
Explanation: "toprac" is the smallest substring in which "toc" can be found.
Input: s = "zoomlazapzo", p = "oza"
Output: "apzo"
Explanation: "apzo" is the smallest substring in which "oza" can be found.
Input: s = "zoom", p = "zooe"
Output: ""
Explanation: No substring is present containing all characters of p.
Constraints: 
1 ≤ s.length(), p.length() ≤ 106
s, p consists of lowercase english letters

Intuition:
Use Sliding Window + Frequency HashMap

We maintain a window in s that:

expands to include characters
shrinks when the condition is satisfied

Variables: 
p_count       -> frequency map of p
window_count  -> frequency map of current window

required = len(p_count)   # number of unique chars needed
formed = 0                # how many chars currently satisfied

left = 0
right = expanding pointer

Expansion:
Move right pointer.
window_count[char] += 1

Check if requirement satisfied:
if char in p_count and window_count[char] == p_count[char]:
    formed += 1

Window Becomes Valid:
formed == required

Window Shrinking:
while left <= right and formed == required:
1️⃣ Update minimum substring

2️⃣ Remove left character

window_count[left_char] -= 1

3️⃣ Check if requirement breaks

if left_char in p_count and window_count[left_char] < p_count[left_char]:
    formed -= 1



Algo:
expand right pointer
    ↓
update window_count
    ↓
if requirement satisfied
    formed += 1
    ↓
while window valid
    update answer
    shrink from left
    if requirement breaks
        formed -= 1
        stop shrinking
    ↓
continue expanding right
'''

from collections import Counter
class Solution:
    def minWindow(self, s, p):
        # code here
        if not s or not p:
            return ""

        p_count = Counter(p)
        required = len(p_count)
    
        left = 0
        formed = 0
        window_count = {}
    
        min_len = float('inf')
        min_start = 0
    
        for right in range(len(s)):
            char = s[right]
            window_count[char] = window_count.get(char, 0) + 1
    
            if char in p_count and window_count[char] == p_count[char]:
                formed += 1
    
            while left <= right and formed == required:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_start = left
    
                left_char = s[left]
                window_count[left_char] -= 1
    
                if left_char in p_count and window_count[left_char] < p_count[left_char]:
                    formed -= 1
    
                left += 1
    
        if min_len == float('inf'):
            return ""
        
        return s[min_start:min_start + min_len]

