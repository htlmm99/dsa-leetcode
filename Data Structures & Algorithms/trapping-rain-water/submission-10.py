class Solution:
    def trap(self, height: List[int]) -> int:
        area = 0
        n = len(height)
        
        for i in range(1, len(height)-1):
            leftmax = max([height[x] for x in range(0, i+1)])
            rightmax = max([height[x] for x in range(i, n)])
            x = min(leftmax, rightmax)
            area += x - height[i]
 
        return area
            
