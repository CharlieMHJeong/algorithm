class Solution:
    def rotate(self, A):
        A[:] = map(list,zip(*A[::-1]))
        return A

    def rotate2(self, A):
        A[:] = zip(A[::-1])
        return A

    def rotate3(self, A):
        A[:] = zip(A)
        return A


A = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]

s = Solution()
print(s.rotate(A))
