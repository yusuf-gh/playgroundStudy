
class Solution:
    def twosum(self, nums: list[int], target: int) -> list[int]:
        hashMap: dict[int, int] = {}

        for i in range(len(nums)):
            cur: int = nums[i]
            # объявляю значение индекса i
            # cur + x = target
            # x = target - cur
            x: int = target - cur
            if x in hashMap:
                return [hashMap.get(x), i]
            # если условие не соблюдено создаем запись
            hashMap[cur] = i

        return []