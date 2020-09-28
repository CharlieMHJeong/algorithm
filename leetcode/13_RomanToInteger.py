# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
#
# Example 1:
# # Input: "III"
# Output: 3

# Example 2:
# # Input: "IV"
# Output: 4

# Example 3:
# Input: "IX"
# Output: 9

# Example 4:
# Input: "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.

# Example 5:
# Input: "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

class Solution:
    def romanToInt(self, s):
        """
        :param s: str
        :return: int
        """
        sum = 0
        prev = 0
        roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

        rs = s[::-1]

        for i in rs:
            curr = roman[i]
            if prev > curr:
                sum -= curr
            else:
                sum += curr
            prev = curr
        return sum

roman_number = 'MCMXCIV'
s = Solution()
r = s.romanToInt(roman_number)
print(r)
