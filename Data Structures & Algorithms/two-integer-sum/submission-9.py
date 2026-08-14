class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = []
        for i, num in enumerate(nums):
            sorted_nums.append([num, i])

        sorted_nums.sort()

        front_pointer, last_pointer = 0, len(nums) - 1
        while(front_pointer < last_pointer):
            if sorted_nums[front_pointer][0] + sorted_nums[last_pointer][0] > target:
                last_pointer -= 1
            elif sorted_nums[front_pointer][0] + sorted_nums[last_pointer][0] < target:
                front_pointer += 1
            else:
                return sorted([sorted_nums[front_pointer][1],sorted_nums[last_pointer][1]])