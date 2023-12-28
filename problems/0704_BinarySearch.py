class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)

        while l < r:
            i = (l + r) // 2
            if nums[i] > target:
                r = i
            elif nums[i] < target:
                l = i+1
            else:
                return i

        return -1