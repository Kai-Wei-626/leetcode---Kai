'''
Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition.

Example 1:

Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
'''

##solution 1
L = [1,2,3,4]

L1 = [x for x in L if x%2 == 0] + [x for x in L if x%2 != 0]
#time complexity = O(2n) = O(n)

##solution 2
i = 0
j = len(L) - 1
while i < j:
    if L[i]%2 > L[j]%2:
        L[i],L[j] = L[j], L[i]
    if L[i]%2 == 0:
        i += 1
    if L[i]%2 == 1:
        j -= 1
#time complexity = O(n)      
