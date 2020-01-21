class Solution:
    # def countAndSay(self, n: int) -> str:
    def countAndSay(self, n):
        """
        :param n: int
        :return: str
        """
        s = '1'
        for i in range(n-1):
            count = 1
            temp=[]
            for j in range(1, len(s)):
                if s[j] == s[j-1]:
                    count += 1
                else:
                    temp.append(str(count))
                    temp.append(s[j-1])
            temp.append(str(count))
            temp.append(s[-1])
            s = "".join(temp)
        return s

s = Solution()
r = s.countAndSay(5)
print(r)
r = s.countAndSay(6)
print(r)
