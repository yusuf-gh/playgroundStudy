class Solution:
    def romanToInt(self, s: str) -> int:
        hashMap: dict[str, int] = {
            "M": 1000,
            "D": 500,
            "C": 100,
            "L": 50,
            "X": 10,
            "V": 5,
            "I": 1
        }

        res = 0
        prev: str = "M"

        for num in s:
            if hashMap[prev] < hashMap[num]:
                res -= hashMap[prev]
                res += (hashMap[num] - hashMap[prev])
            else:
                res += hashMap[num]
            prev = num
        return res

