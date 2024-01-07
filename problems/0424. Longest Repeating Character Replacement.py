from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = defaultdict(int)
        l = 0
        ans = 0

        for i in range(len(s)):
            d[s[i]] += 1

            freq_char_count = max(d.values())

            if (i - l + 1) - freq_char_count <= k:
                ans = max(ans, i-l+1)
            else:
                d[s[l]] -= 1
                l += 1

        return ans