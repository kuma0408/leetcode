from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.d = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        li = self.d[key]
        l = 0
        r = len(li) - 1
        ret = ""

        while l <= r:
            mid = (l+r) // 2
            if li[mid][1] == timestamp:
                return li[mid][0]
            elif li[mid][1] < timestamp:
                ret = li[mid][0]
                l = mid + 1
            else:
                r = mid - 1

        return ret

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)