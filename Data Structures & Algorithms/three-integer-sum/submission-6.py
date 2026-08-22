class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []

        for i in range(len(nums)):
            target = -nums[i]

            p1 = i + 1
            p2 = len(nums) - 1

            while(p1 < p2):
                if i != 0 and nums[i] == nums[i-1]:
                    break
                if nums[p1] + nums[p2] > target : 
                    p2 -= 1
                elif nums[p1] + nums[p2] < target : 
                    p1 += 1
                else:
                    l = (nums[i], nums[p1], nums[p2])
                    if l not in res:
                       res.append(l)
                    p1 += 1
                    p2 -= 1
        return res