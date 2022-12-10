"""
Given an array of integers, return a new array such that each element at index i of the new array is the product of all
the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was
[3, 2, 1], the expected output would be [2, 3, 6].
"""
from functools import reduce
from itertools import combinations
input_given = [1, 2, 3, 4, 5, -10]

# option 1 --> skipping each element , by making use of combination
b = list(combinations(input_given, len(input_given)-1))[::-1]
c = list(map(lambda x: list(x), b))
d = [reduce(lambda x,y:x*y, i) for i in c]
print(d)

# option 2 --> multiply all the elems from input and then divide each
total_prod = reduce(lambda x,y:x*y, input_given)
ans = [int(total_prod/ele) for ele in input_given]
print(ans)




