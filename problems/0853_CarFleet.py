class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = []
        for p, s in zip(position, speed):
            pair.append((p, s))
        
        # 現在地がゴールから遠い順にソートする
        pair = sorted(pair, key=lambda x: x[0])

        ans = 0
        while len(pair) > 0:
            top = pair.pop()
            time_to_goal = ((target - top[0]) / top[1])
            while len(pair) > 0 and ((target - pair[-1][0]) / pair[-1][1]) <= time_to_goal:
                pair.pop()
            ans += 1

        return ans

