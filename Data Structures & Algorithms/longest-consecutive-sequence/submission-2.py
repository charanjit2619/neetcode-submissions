class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        sorted_nums = sorted(set(nums))
        res = 1

        max_length = 1

        for i in range(len(sorted_nums) - 1):
            if sorted_nums[i+1] - sorted_nums[i] == 1:
                max_length += 1
            
            else:
                max_length = 1
            res = max(res, max_length)

        return res