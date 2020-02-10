class Solution:
    # def lengthOfLastWord(self, s: str) -> int:
    def lengthOfLastWord(self, str):

        if len(str) == 0:
            return 0
        else:
            # return len(str.strip().split(' ')[-1])
            str_list = str.strip().split(' ')
            last_word = str_list[-1]
            l= len(last_word)
            return l
