class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ngrams = defaultdict(list)

        for word in strs:
            ngrams["".join(sorted(word))].append(word)
        res = []
        for key in ngrams.keys():
            res.append(ngrams[key])

        return res