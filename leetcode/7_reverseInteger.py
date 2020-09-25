def cmp(a, b):
    return (a > b) - (a < b)

class Solution:
    def reverse(self, x):
        s = cmp(x, 0)
        # print("Sign: {}".format(s))
        x = abs(x)
        x = str(x)[::-1]
        # print("reversed: {}".format(x))
        r = int(x)
        r = s* r * (r < 2**31)
        return r

x = -2147483648

print(type(x))
s = Solution()
print(s.reverse(x))
