class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for i in range(len(nums)):
            freq[nums[i]] += 1
        
        freq_list = []
        for key, val in freq.items():
            freq_list.append([val, key])
        
        freq_list.sort(reverse = True)

        res = []
        for i in range(k):
            res.append(freq_list[i][1])
        return res