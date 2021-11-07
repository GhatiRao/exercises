"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".


Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

"""

# class Solution:
#     def longestCommonPrefix(self, strs) -> str:
#         #strs = sorted(strs, key = lambda x: len(x))
#         strs.sort(key=lambda s: len(s))
#         for i in range(len(strs[0])):
#             for sen in strs:
#                 if sen[i] != strs[0][i]:
#                     return strs[0][0:i]
#         return strs[0]

class Solution:
    def longestCommonPrefix(self, strs) -> str:
        # strs.sort(key=lambda s: len(s))
        # for l in range(len(strs[0])):
        #     for m in strs[1:]:
        #         if m[l] != strs[0][l]:
        #             return strs[0][l-1]
        # #return strs[0]

        i = 0
        for s in zip(*strs):
            if len(set(s)) != 1: break
            else:
                i += 1
        return strs[0][0:i]


c = Solution()
print(c.longestCommonPrefix(["dog","dog","flight"]))




# a = 'hello'
# b = 'hi'
# c = a+b
# print(c)
#
# # di = { }
# # for e in c:
# #     di[e] = c.count(e)
# # print(di)
#
# print(dir(set))
# print(list(set(a).intersection(set(b))))




