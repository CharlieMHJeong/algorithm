class Solution:
    # def strStr(self, haystack: str, needle: str) -> int:
    def strStr(self, haystack, needle):
        """
        :param haystack: str
        :param needle: str
        :return: int
        """
        return haystack.find(needle)

s = Solution()
r = s.strStr('hello', 'll')
print(r)
