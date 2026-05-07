class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums = sorted(nums)
        n = len(nums)
        for x in range(0, n):
            if nums[x] > 0:
                break
            flag = 0 - nums[x]
            left, right = x+1, n-1
            while left < right:
                if nums[left] + nums[right] == flag:
                    if [nums[x], nums[left], nums[right]] not in result: 
                        result.append([nums[x], nums[left], nums[right]])
                    right -= 1
                    left +=1 
                elif nums[left] + nums[right] > flag:
                    right -= 1
                else:
                    left +=1 
        return result 