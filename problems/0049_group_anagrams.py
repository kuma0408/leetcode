import collections

# https://leetcode.com/problems/group-anagrams/description/
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ret = []
        d = collections.defaultdict(list)
        for s in strs:
            d["".join(sorted(s))].append(s)

        return d.values()