# https://leetcode.com/problems/valid-parentheses/
class Solution:
    def isValid(self, s: str) -> bool:
        li = []
        for char in s:
            if len(li) == 0:
                li.append(char)
                continue

            if li[-1] + char in ("[]", "{}", "()"):
                li.pop()
            else:
                li.append(char)

        return li == []