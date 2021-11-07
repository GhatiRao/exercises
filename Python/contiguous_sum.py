"""
Given an array of numbers, find the maximum sum of any contiguous subarray of the array.

For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137,
since we would take elements 42, 14, -5, and 86.

Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would not take any elements.
Do this in O(N) time.
"""
# print(summ([34, -50, 42, 14, -5, 86]))
# print(summ([42, 14, -5, 86]))

# 1. Brute Force:
# Traverse through the entire list of values, by taking each element as beginning
chain = [34, -50, 42, 14, -5, 86]
# for i in range(len(chain)):
#     sum_ini = chain[i]
#     for j in range(i+1, len(chain)):
#         sum = sum_ini + chain[j]
#         print(f"{sum_ini} + {chain[j]} = {sum}")
#         sum_ini = sum
#     break


"""
The Logic is:
If the sum of current index and the next index results in a negative number, end this summation.
So, while the sum ( which is taken to be the current index ) is a positive number, keep adding the next number.

"""


def contigous_sum(chain: list[int]) -> int:
    greater_sum = []
    if sum(chain) < 0 or not chain:
        #print(f"this is the greater sum: 0")
        return 0
    else:
        for i in range(1, len(chain)):
            summ = chain[i - 1]
            #print(f"here at {summ}")
            while summ >= 0 and i <= len(chain) - 1:
                #print(f"index is {i}")
                summ += chain[i]
                #print(summ)
                i += 1
            greater_sum.append(summ)
    # print(f"this is the greater sum: {greater_sum}")
    # print(f"maximum sum is: {max(greater_sum)}")
    return max(greater_sum)

test = [34, -50, 42, 14, -5, 86]
print(f"final number is: {contigous_sum(test)}")

