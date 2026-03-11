'''
Question:
You are given an array citations[], where each element citations[i] represents the number of citations received by the ith paper of a researcher. 
You have to calculate the researcher’s H-index. The H-index is defined as the 
maximum value H, such that the researcher has published  at least H papers, 
and all those papers have citation value greater than or equal to H.

Input: citations[] = [3, 0, 5, 3, 0]
Output: 3
Explanation: There are at least 3 papers
with citation counts of 3, 5, and 3, all having citations greater than or equal to 3.

Input: citations[] = [5, 1, 2, 4, 1]
Output: 2
Explanation: There are 3 papers (with citation counts of 5, 2, and 4) that have 2 or more citations.
However, the H-Index cannot be 3 because there aren't 3 papers with 3 or more citations.

Understanding:
You are given an array:
citations[i] = number of citations of the ith paper

You must find the H-index.
"Definition of H-index":
H-index is the maximum number H such that::
    The researcher has at least H papers
    and each of those H papers has at least H citations.

IMPORTANT:
We want the largest possible H
Not just any H that works


So basically we wnat to find an index and that index should have at least arr[i]>= i
For suppose say we have 

arr = 5, 1, 2, 4, 1

Now say index is 1 so H = 1,
do we have atleast one research paper where it is greater than or equals to 1
yes --> [5,1,2,4,1]>= 1

Now index is 2, H=2
do we have atleast 2 research paper where it is greater than or equals to 2
yes --> [5,2,4]>= 2 total 3 research papers

Next index is 3, H=3
do we have atleast 3 research paper where it is greater than or equals to 3
yes --> [5,2,4] > =3

Next index is 4, H=4
do we have atleast 4 research paper where it is greater than or equals to 4
No --> only have [5,4] so fails 

Now maximum H is 3 so return 3.

Intuition:

1. Sort the array in descending order
2. Once sorted, check for the index i does the citation of that arr[i] index 
should be greater than or equal if not we can stop.

But wait why?
suppose say we have 5 students and their marks

[95, 80, 70, 30, 20]

Now ask,
can we  say atleast 3 students scored  80 marks 
now we can directly check student 3 if he has 80 marks or not if he doesn't that means 
we dont have atleast 3 who scored 80 may be other two might score but we need atleast 3.

so for above index 
we check if arr[i] >= i
'''

class Solution:
    def hIndex(self, citations):
        #code here
        citations.sort(reverse=True)
        h = 0
        for i in range(len(citations)):
            if citations[i] >= i+1:
                h = i+1
            else:
                break
        return h