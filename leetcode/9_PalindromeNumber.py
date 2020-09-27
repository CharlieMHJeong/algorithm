#PalindromNumber
# example1
# Input: 121
# Output: true
#
# example2
# Input: -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        # Getting the range of the number
        r = 1
        while x / r >= 10:
            r *= 10

        while r > 1:
            left, x = divmod(x, r)    # Took out the most left digit and assign it to left
            x, right = divmod(x, 10)  # Took out the most right digit and assign it to right          
            if left != right:         #Compare the right and left
                return False
            r //=100                  #
        return True


s = Solution()
r = s.isPalindrome(234432)
print(r)
