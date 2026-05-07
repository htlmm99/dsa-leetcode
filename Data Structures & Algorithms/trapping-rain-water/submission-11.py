class Solution:
    def trap(self, height: List[int]) -> int:
        area = 0
        n = len(height)
        l, r = 0, n-1
        leftmax = height[l]
        rightmax = height[r]

        while l < r:
            if leftmax < rightmax:
                l+=1
                leftmax = max(leftmax, height[l])
                area+= leftmax - height[l]
            else:
                r-=1
                rightmax = max(rightmax, height[r])
                area+= rightmax - height[r]
        return area
            
