class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, val in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while(l < r):
                if l > i + 1 and nums[l] == nums[l-1]:
                    l += 1
                    continue
                if val + nums[l] + nums[r] == 0:
                    res.append([val, nums[l], nums[r]])
                    l += 1
                    r -= 1
                elif val + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    r -= 1
        return res

                    

            