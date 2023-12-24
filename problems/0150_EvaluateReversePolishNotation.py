# https://leetcode.com/problems/evaluate-reverse-polish-notation/
import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        li = []
        for token in tokens:
            if token in ("+", "-", "*", "/"):
                second_num = li.pop()
                first_num = li.pop()
                if token == "/":
                    ans = eval(str(first_num) + token + str(second_num))
                    ans = math.floor(ans) if ans >= 0 else math.ceil(ans)
                else:
                    ans = eval(str(first_num) + token + str(second_num))
                li.append(ans)
            else:
                li.append(token)

        return int(li[0])