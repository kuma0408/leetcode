class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_num = 5001
        l = 0
        r = len(nums)-1

        while l <= r:
            r_val = nums[r]
            mid = (l+r) // 2

            if nums[mid] < r_val:
                min_num = min(min_num, nums[mid])
                r = mid - 1
            else:
                min_num = min(min_num, nums[mid])
                l = mid + 1

        return min_num