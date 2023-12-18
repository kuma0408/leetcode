# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        front = len(numbers) -1
        back = 0
        
        while True:
            tmp_sum = numbers[front] + numbers[back]
            if tmp_sum == target:
                return [back+1, front+1]
            elif tmp_sum >= target:
                front -= 1
            else:
                back += 1