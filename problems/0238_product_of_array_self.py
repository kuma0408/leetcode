# https://leetcode.com/problems/product-of-array-except-self/
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        li = [nums[0]]

        prod = nums[0]
        for i in range(1, len(nums)):
            prod *= nums[i]
            li.append(prod)

        back_li = [nums[-1]]
        prod = nums[-1]
        for i in range(2, len(nums)+1):
            prod *= nums[-i]
            back_li.append(prod)

        ret = []
        back_li = list(reversed(back_li))
        for i in range(len(nums)):
            if i == 0:
                ret.append(back_li[1])
            elif i == len(nums)-1:
                ret.append(li[i-1])
            else:
                ret.append(li[i-1] * back_li[i+1])
        return ret