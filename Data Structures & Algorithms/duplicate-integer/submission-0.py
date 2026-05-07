class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = {}
        for x in nums:
            if x in count:
                count[x] +=1
                return True
            else:
                count[x] = 1
        return False
        