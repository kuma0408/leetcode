# https://leetcode.com/problems/longest-consecutive-sequence/
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        if len(s) == 0:
            return 0

        max_len = 1
        len_count = 1
        n = 1
        front_flg = True
        back_flg = True

        start = s.pop()

        while(len(s) > 0):
            if front_flg and start + n in s:
                s.discard(start+n)
                len_count += 1
            else:
                front_flg = False

            if back_flg and start - n in s:
                s.discard(start-n)
                len_count += 1
            else:
                back_flg = False

            n += 1

            if not front_flg and not back_flg:
                max_len = max(max_len, len_count)
                len_count = 1
                front_flg = True
                back_flg = True
                n = 1
                start = s.pop()

        max_len = max(max_len, len_count)
        return max_len