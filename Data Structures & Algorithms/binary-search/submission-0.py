class Solution:
    def search(self, nums: List[int], target: int) -> int:
        p1 = 0
        p2 = len(nums) - 1

        while(p1 <= p2):
            idx = (p1 + p2) // 2

            if target == nums[idx]:
                return idx
            elif target < nums[idx]:
                p2 = idx - 1
            elif target > nums[idx]:
                p1 = idx + 1


        return -1