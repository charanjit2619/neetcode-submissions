class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = defaultdict(int)

        for num in nums:
            freq_map[num] += 1
        
        res = []
        for num, freq in freq_map.items():
            res.append([freq, num])

        res.sort(reverse = True)
        res1 = []
        for i in res[:k]:
            res1.append(i[1])
        return res1
