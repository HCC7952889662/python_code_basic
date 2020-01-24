class Solution:
    def threeSum(self, nums: [int]):
        result = set()
        nums.sort()
        length = len(nums)

        for i in range(1, len(nums)-2):
            if nums[i] > 0:
                break
            if nums[i] == nums[i-1]:
                continue
            l, r = i+1, length-1
            while l<r:
                total = nums[i]+nums[l]+nums[r]
                if total<0:
                    l+=1
                elif total>0:
                    r-=1
                else:
                    result.add(tuple([nums[i], nums[l], nums[r]]))
                    l+=1
                    r-=1
        return list(result)

nums = [-1,0,1,2,-1,-4]
#print(prices[1:2])
print(Solution().threeSum(nums))
