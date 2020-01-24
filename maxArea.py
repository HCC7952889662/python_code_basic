class Solution:
    def maxArea(self, height: [int]) -> int:
        #2 pointers
        right = len(height) - 1
        left = 0
        #Return Value
        MaxArea = 0
        #Flag
        l = 0
        r = 0
        while left < right:
            if height[left] < height[right]:
                area = height[left] * (right - left)
                left += 1
                l = 1
            else:
                area = height[right] * (right - left)
                right -= 1
                r = 1
            # decrease the times for multiplication
            if area > MaxArea:
                MaxArea = area
                if l == 1:
                    while height[left-1] > height[left]:
                        left+=1;
                        l = 0;
                if r == 1:
                    while height[right+1] > height[right]:
                        right-=1;
                        r = 0;
        return MaxArea

height = [1,8,6,2,5,4,8,3,7]
#print(prices[1:2])
print(Solution().maxArea(height))
