# https://leetcode.com/problems/top-k-frequent-elements/
import collections
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        d = collections.defaultdict(list)

        # 出現回数を降順にソート
        count_list = sorted(counter.values(), reverse=True)
        # 上位k件のみを取得
        target = set(count_list[:k])

        ret = []
        for key, value in counter.items():
            if value in target:
                ret.append(key)
        
        return ret