 #basic's of oops
class college:
    def __init__(self,name,course):
        self.n=name
        self.c=course
    def hi(self):
        print(self.n,self.c)
c=college('psg','cse')
c.hi()

class Solution:
    def isPalindrome(self, x: int):
        if x < 0:
            return 'false'
        ans = x
        n = 0
        while x != 0:
            n = n * 10
            n += x % 10
            x = x // 10
        if ans==n:
            return 'true'
        return 'false'
x = int(input("Enter"))
a = Solution().isPalindrome(x)
print(a)

