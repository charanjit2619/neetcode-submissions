class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for word in strs:
            sorted_word = sorted(word)
            if "".join(sorted_word) in anagrams:
                anagrams["".join(sorted_word)].append(word)
            else:
                anagrams["".join(sorted_word)] = [word]
        return list(anagrams.values())
