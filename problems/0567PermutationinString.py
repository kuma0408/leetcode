from collections import defaultdict
import copy
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d = defaultdict(int)
        for s in s1:
            d[s] += 1
        tmp_d = copy.copy(d)
        l = 0

        for i in range(len(s2)):
            if s2[i] in s1:
                tmp_d[s2[i]] -= 1
                while min(tmp_d.values()) < 0:
                        tmp_d[s2[l]] += 1
                        l += 1
                if max(tmp_d.values()) == 0:
                    return True
            else:
                l = i+1
                tmp_d = copy.copy(d)

        return False