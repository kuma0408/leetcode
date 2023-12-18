# https://leetcode.com/problems/3sum/
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = []
        s = set(nums)
        while len(s) > 0:
            target = s.pop()
            skip_set = set()
            for element in s:
                if element in skip_set:
                    continue

                if -(element+target) in s:
                    ret.append([target, element, -(element+target)])
                    skip_set.add(-(element+target))

        return ret