# https://leetcode.com/problems/3sum/
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = []
        nums = sorted(nums)

        for i, num in enumerate(nums):
            if num > 0:
                break

            # To avoid dupulicated answer, skip the same value as the previous one.
            if i > 0 and (num == nums[i-1]):
                continue
            l = i+1
            r = len(nums)-1

            while l < r:
                tmp_sum = num + nums[l] + nums[r]

                if tmp_sum == 0:
                    ret.append([num, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                elif tmp_sum >= 0:
                    r -= 1
                else:
                    l += 1

        return ret