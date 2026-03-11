'''
Maximum number of overlapping Intervals
You are given an array of intervals arr[][], where each interval is represented by 
two integers [start, end] (inclusive). Return the maximum number of
intervals that overlap at any point in time.

Examples :

Input: arr[][] = [[1, 2], [2, 4], [3, 6]]
Output: 2
Explanation: The maximum overlapping intervals are 2(between (1, 2) and (2, 4) or 
between (2, 4) and (3, 6))

1-----------2
            2-------------4
               3-------------------6

At t-->1, overlap =1
At t-->2, overlap =2
At t-->3, overlap = 2
At t-->4, overlap = 2
At t-->5, overlap = 1
At t-->6, overlap = 1
Max overlap = 2

Brute Force:
Outer loop is for t where for(max_start, max_end)
Inner loop is to check if this t in is start and end interval for each i
min_start = min(interval[0] for interval in arr) 
max_end = max(interval[1] for interval in arr) 
max_overlap = 0 # To store the maximum overlap found 
# Step 2: Check every time point in the range 
for t in range(min_start, max_end + 1): 
    count = 0 # Count intervals active at time t 
    # Step 3: Check all intervals 
    for start, end in arr: 
        if start <= t <= end: # Inclusive condition 
            count += 1 
    # Step 4: Update maximum 
    max_overlap = max(max_overlap, count)
arr = [[1,5],[2,6],[4,8]]
min_start = 1
max_end   = 8

At t=1
we check
[1,5] ✔

[2,6] ✘

[4,8] ✘

Count = 1
max = 1

t=2
Active:

[1,5] ✔

[2,6] ✔

[4,8] ✘

Count = 2
max = 2

t=3
t = 3

Active:

[1,5] ✔

[2,6] ✔

[4,8] ✘

Count = 2
max = 2



Two pointers:
[1,5]
[2,6]
[4,8]

sort 
start time: [1,2,4]
end time:[5,6,8]
What happens next in time?
    A person entering?
    Or a person leaving? 

>>>>Next entry time   vs   Next exit time
    Whichever is smaller happens first.   
Step 1
1 ≤ 5 → current = 1 → max = 1
Step 2
Next entry is at 2 and end is still 5
2 <= 5
current = 2 another event came 
max = 2
Next entry is 4 and end is 5  
4 <= 5
current = 3
max = 3
Next entry is 9 where end is 5 
so on this entry one interval got ended
as 9 > 5
so current overlap is decreased as one interval is done at this entry 
current = 2
similarly for 9 > 6
another interval is done 
=============Algorithm==========
starts = sorted([i[0] for i in intervals])
    ends = sorted([i[1] for i in intervals])

    i = j = 0
    current = 0
    max_overlap = 0
    n = len(intervals)

    while i < n and j < n:
        if starts[i] <= ends[j]:
            current += 1
            max_overlap = max(max_overlap, current)
            i += 1
        else:
            current -= 1
            j += 1
================================
Sweep line Method:

Convert intervals into events:
(start, +1)
(end+1, -1) ← important trick

Sort all events
Traverse and keep running sum.

Dry run:
[1,5]
[2,6]
[4,8]

(1, +1)
(6, -1)

(2, +1)
(7, -1)

(4, +1)
(9, -1)

sort
(1, +1)
(2, +1)
(4, +1)
(6, -1)
(7, -1)
(9, -1)

Step 3 — Traverse
| Time | Change | Current | Max |
| ---- | ------ | ------- | --- |
| 1    | +1     | 1       | 1   |
| 2    | +1     | 2       | 2   |
| 4    | +1     | 3       | 3   |
| 6    | -1     | 2       | 3   |
| 7    | -1     | 1       | 3   |
| 9    | -1     | 0       | 3   |

'''

#Sweep line optimal
def max_overlap_sweepline(intervals):
    events = []

    for start, end in intervals:
        events.append((start, 1))
        events.append((end + 1, -1))  # +1 handles inclusive case

    events.sort()

    current = 0
    max_overlap = 0

    for time, change in events:
        current += change
        max_overlap = max(max_overlap, current)

    return max_overlap