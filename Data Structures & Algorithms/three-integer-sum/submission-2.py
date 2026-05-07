class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        n = len(nums)

        for x in range(n):

            if x > 0 and nums[x] == nums[x - 1]:
                continue

            flag = -nums[x]
            left, right = x + 1, n - 1

            while left < right:
                s = nums[left] + nums[right]

                if s == flag:
                    result.append([nums[x], nums[left], nums[right]])

                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif s > flag:
                    right -= 1
                else:
                    left += 1

        return result