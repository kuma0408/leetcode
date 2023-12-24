# https://leetcode.com/problems/min-stack/description/
class MinStack:

    def __init__(self):
        self.li = []
        self.min_li = []
        self.min = 2 ** 31

    def push(self, val: int) -> None:
        self.li.append(val)
        if self.min >= val:
            self.min_li.append(val)
            self.min = val
        else:
            self.min_li.append(self.min)

    def pop(self) -> None:
        self.li.pop()
        self.min_li.pop()
        if len(self.li) == 0:
            self.min = 2 ** 31
        else:
            self.min = self.min_li[-1]

    def top(self) -> int:
        return self.li[-1]

    def getMin(self) -> int:
        return self.min_li[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()