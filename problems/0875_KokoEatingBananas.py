import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = math.ceil(sum(piles) / h)
        r = max(piles)
        ans = r

        while l <= r:
            mid = (l+r) // 2
            total_h = 0
            for i in piles:
                total_h += math.ceil(i / mid)
                if total_h > h:
                    break
            
            if total_h > h:
                l = mid + 1
            else:
                ans = min(ans, mid)
                r = mid - 1

        return ans