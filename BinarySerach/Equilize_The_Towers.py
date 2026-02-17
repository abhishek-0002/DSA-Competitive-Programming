'''
Question:
You are given an array heights[] representing the heights of towers and another array cost[] where each element represents the cost of modifying the height of respective tower.

The goal is to make all towers of same height by either adding or removing blocks from each tower.
Modifying the height of tower 'i' by 1 unit (add or remove) costs cost[i].
Return the minimum cost to equalize the heights of all the towers.

Examples:
Input: heights[] = [1, 2, 3], cost[] = [10, 100, 1000]
Output: 120
Explanation: The heights can be equalized by either "Removing one block from 3 and adding 
one in 1" or "Adding two blocks in 1 and adding one in 2". Since the cost of operation in 
tower 3 is 1000, the first process would yield 1010 while the second one yields 120.

Input: heights[] = [7, 1, 5], cost[] = [1, 1, 1]
Output: 6
Explanation: The minimum cost to equalize the towers is 6, 
achieved by setting all towers to height 5.
'''



'''
Intuition:
heights[] = [1,100] cost[] = [1,1]

Make all the towers of same height either by removing blocks from each tower
Modifying the height of tower i by  1 unit costs cost[i]

To make the heights equal we can add 99 to h[i] so the cost will be 99*1=99

heights[] = [1,2,3] cost[] = [10, 100, 1000]

H1 weighted median height: h[1] = 1

To make h[2] = 2 to 1 
h[3] = 3 to 1
Cost of h[2] to 1  is 1*100 = 100
cost of h[3] to 1  is 2*100 = 1000
cost of total operation is = 1010

H2 weighted median  : h[2] = 2
To make h[1] = 1 to 2
h[3] = 3 to 2 
Cost of h[1] to 2 is 1*10 = 10
Cost of h[3] to 2 is 1*1000 = 1000
1010

H3 weighted median  : h[3] = 3
To make h[1] to 3 
h[2] to 3
cost of h[1] to 3 is 2*10 = 20
cost of h[2] to 3 is 1*100 = 120
total = 120

Sum f(H)= ∑|H-h[i]|*cost[i]
 
H is the weighted height we need to choose

so if we choose height H with Weighted Median 

But why?

First sort towers by height
Think of cost[i] as the weight of each height.

Imagine each tower is pulling H toward itself with force = cost[i].

We want the point where:

Total pulling force from left = Total pulling force from right

That balancing point is the weighted median.


Mathematical Explanation
Let total weight:
W=∑cost[i]
The optimal height H is the first height where:

prefix cost ≥ 𝑊/2
Consider moving H slightly to the right.

Change in cost depends on:

Towers left of H → cost increases
Towers right of H → cost decreases

Slope of cost function:
slope = (total weight on left) − (total weight on right)


Why Cumulative Sum Near Half Works
you are effectively finding the point where:

cumulative cost ≈ 𝑡𝑜𝑡𝑎𝑙 𝑐𝑜𝑠𝑡/2

That ensures:
Left side weight ≤ half
Right side weight ≤ half
''' 

def minCost(heights, cost):
    # code here
    # sort the towers height 
    towers = sorted(zip(heights, cost))
    total_weight = sum(cost)
    cumulative = 0
    weighted_median = 0

    for h, c in towers:
        cumulative += c
        if cumulative >= (total_weight + 1) // 2:
            weighted_median = h
            break

    min_cost = 0
    for h, c in zip(heights, cost):
        min_cost += abs(h - weighted_median) * c

    return min_cost

heights = [1, 2, 10]
cost = [1, 1, 100]
print(minCost(heights, cost))