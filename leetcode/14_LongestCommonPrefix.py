# Find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
# All given inputs are in lowercase letters a-z.

class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        shortest = min(strs, key=len)

        for i, ch in enumerate(shortest):
            for str in strs:
                if str[i] != ch:
                    return shortest[:i]
        return shortest

strs = ["flower","flow","flight"]
# strs = ["dog","racecar","car"]

s = Solution()
r = s.longestCommonPrefix(strs)
print(r)
