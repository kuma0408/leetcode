class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        tmp_d = {}
        l = 0
        r = 0
        ans = 0

        while r < len(s):
            if s[r] in tmp_d:
                ans = max(ans, (r-l))
                idx = tmp_d[s[r]]
                while l < idx + 1:
                    del tmp_d[s[l]]
                    l += 1

            tmp_d[s[r]] = r
            r += 1

        ans = max(ans, (r-l))
        return ans