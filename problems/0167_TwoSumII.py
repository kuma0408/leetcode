# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = {}
        for idx, num in enumerate(numbers):
            if target - num in d:
                return [d[target-num], idx+1]
            d[num] = idx+1