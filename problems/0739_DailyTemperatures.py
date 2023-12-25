class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            if len(stack) == 0:
                stack.append((i, t))
                continue
            
            while len(stack) > 0 and t > stack[-1][1]:
                comb = stack.pop()
                ans[comb[0]] = i - comb[0]

            stack.append((i, t))

        return ans