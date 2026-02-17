# Accuracy: 18.60%

# Geek wants to create a string from the characters of s of size n, but he wants to make sure that no character appears more than k times consecutively in the new string. Find the lexographically largest string Geek could create

# code her sorted str

# dct Coun

# new_str

# for key, va

# times

# new sti

# return new

# Note: Using all the characters from s is not mandatory.

# Example 1:

# Input:

# n 5 k2 5 "zzaaa"

# Output:

# Explanation:

# The lexographically largest that string Geek could create with no character appearing more than k times consecutively is "zzaa"


# methods used: sorted,ord,Counter,min


from collections import Counter
class Solution:
    def createString(self, n : int, k : int, s : str) -> str:
        # code here
        sorted_str = "".join(sorted(s,reverse=True))
        dct = Counter(sorted_str)
        new_str =""
        for key,val in dct.items():
            times_to_join = min(k, val)
            new_str += key*times_to_join
        return new_str
obj = Solution()
print(obj.createString(2,1,"cb"))

