
nums = [11,7,15,17,19,133,123124,123,11123,2]
target = 123124 + 11



class Solution:
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target

    def twoSum(self):
        h = {}
        for i in range(len(self.nums)):
            if self.target - self.nums[i] in h:
                return [h[self.target - self.nums[i]], i]
            h[self.nums[i]] = i
        return [-1, -1]


S1 = Solution(nums, target)
print(S1.twoSum())
