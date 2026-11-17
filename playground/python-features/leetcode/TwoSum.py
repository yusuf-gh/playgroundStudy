

def twosum(nums, target):
    for index1 in range(len(nums)):
        for index2 in range(len(nums)):
            if nums[index1] + nums[index2] == target and index1 != index2:
                return [index1, index2]

    return []