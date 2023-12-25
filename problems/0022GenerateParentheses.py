# https://leetcode.com/problems/generate-parentheses/description/
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        li = []

        def temp(n, s, l, r):
            if len(s) == n*2:
                li.append(s)

            if l < n:
                temp(n, s+"(", l+1, r)
            
            if r < l and r < n:
                temp(n, s+")", l, r+1)
            

        temp(n, "(", 1, 0)

        return li