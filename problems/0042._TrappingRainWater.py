# https://leetcode.com/problems/trapping-rain-water/description/
class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        max_l = height[l]
        max_r = height[r]
        amount = 0

        while l < r:
            if max_l < max_r:
                l += 1
                if height[l] < max_l:
                    amount += (max_l - height[l])
                else:
                    max_l = height[l]
            else:
                r -= 1
                if height[r] < max_r:
                    amount += (max_r - height[r])
                else:
                    max_r = height[r]                

        return amount