# Find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
# All given inputs are in lowercase letters a-z.

class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        #find the shortest word from the list
        shortest = min(strs, key=len)


        #go through each character in the shortest
        for i, ch in enumerate(shortest):
            #From the Each word in the list
            for str in strs:
                #compare each character with the each char in the shortest
                if str[i] != ch:
                    return shortest[:i]
        return shortest

strs = ["flower","flow","flight"]
# strs = ["dog","racecar","car"]

s = Solution()
r = s.longestCommonPrefix(strs)
print(r)
