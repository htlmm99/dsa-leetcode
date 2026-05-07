class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights)-1
        max = 0
        while left < right: 
            amount = (right - left) * min(heights[left], heights[right])
            if amount > max:
                max = amount
            if heights[left] < heights[right]:
                left +=1
            else:
                right -=1

        return max 
        